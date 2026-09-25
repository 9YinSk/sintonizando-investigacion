export const meta = {
  name: 'serie-en-equipo-fable',
  description: 'Igual que serie-en-equipo pero sin tipos de agente registrados: cada agente lee su .claude/agents/<rol>.md y corre con el modelo de la sesion (p. ej. Fable). args: {lote: "G", max: 6} o {ids: [...]}, y opcional esfuerzo: {inv, red, aux}',
  whenToUse: 'Cuando el jefe tiene la herramienta Workflow: lanza y encadena las series de un lote sin que el jefe gaste tokens leyendo y decidiendo.',
  phases: [
    { title: 'Plan', detail: 'siguiente.py y hermanas.py deciden qué toca y en qué modo' },
    { title: 'Recolectar', detail: 'datos gratis para las series nuevas' },
    { title: 'Investigar', detail: 'un investigador en Sonnet por rol' },
    { title: 'Redactar', detail: 'el redactor en Opus (y un reparo si falta algo)' },
    { title: 'Cerrar', detail: 'revisar.py, subir.sh y el estado en lotes/<L>.md' },
  ],
}
const ROLES = ['imagen', 'video', 'voz', 'texto']
// sin agentType: el agente lee su ficha de rol y corre con el modelo de la sesión
const ROL = r => `Eres el subagente «${r}». Antes de nada lee entero /home/user/sintonizando-investigacion/.claude/agents/${r}.md y sigue sus instrucciones como si fueran tu prompt de sistema (ignora su línea model: usas el modelo de esta sesión). Encargo: `
// esfuerzo por rol (args.esfuerzo = {inv: 'medium', red: 'high', aux: 'low'}); sin él, el de la sesión
const EF = (args && args.esfuerzo) || {}
const PLAN = { type: 'object', properties: { items: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, lote: { type: 'string' }, modo: { type: 'string' }, relanzar: { type: 'array', items: { type: 'string' } }, faltan: { type: 'array', items: { type: 'string' } }, hermana: { type: 'string' }, biblia_existe: { type: 'boolean' } }, required: ['id', 'lote', 'modo', 'relanzar', 'faltan', 'biblia_existe'] } } }, required: ['items'] }
const INV = { type: 'object', properties: { sigue_pendiente: { type: 'boolean' }, resumen: { type: 'string' } }, required: ['sigue_pendiente', 'resumen'] }
const RED = { type: 'object', properties: { resumen: { type: 'string' }, avisos: { type: 'string' } }, required: ['resumen'] }
const CIERRE = { type: 'object', properties: { completa: { type: 'boolean' }, falta: { type: 'string' }, subido: { type: 'boolean' } }, required: ['completa', 'falta', 'subido'] }
const OK = { type: 'object', properties: { ok: { type: 'boolean' }, aviso: { type: 'string' } }, required: ['ok'] }
const FLOJAS = { type: 'object', properties: { flojas: { type: 'array', items: { type: 'object', properties: { rol: { type: 'string' }, por_que: { type: 'string' } }, required: ['rol'] } } }, required: ['flojas'] }

async function seguro(fn) { try { return await fn() } catch (e) { log(`error de agente: ${String(e).slice(0, 200)}`); return null } }
const hermana = it => it.hermana ? ` Serie hermana (misma obra, otro encargo): ${it.hermana}.` : ''

phase('Plan')
const lote = (args && args.lote) ? String(args.lote).toUpperCase() : ''
const max = (args && args.max) ? Number(args.max) : 6
const ids = (args && args.ids) ? args.ids : []
const plan = await agent(`En /home/user/sintonizando-investigacion decide qué series tocan. ${ids.length ? `Sólo estas: ${ids.join(', ')}. Corre \`python3 herramientas/siguiente.py 200${lote ? ' --lote ' + lote : ''}\` y quédate con sus líneas.` : `Corre \`python3 herramientas/siguiente.py ${max}${lote ? ' --lote ' + lote : ''}\` y toma esas líneas en ese orden.`} Cada línea es «<id> <modo> <por qué>». Para cada una: relanzar = roles tras «partes a medias:»; faltan = roles tras «faltan roles:»; biblia_existe = true si el «por qué» no dice «sin biblia»; lote = la letra (${lote || 'A-H según REPARTO.md: A 02-05 y 31-36, B 06-18, C 19-30, D 37-56, E 57-76, F 77-96, G 97-116, H 117-131'}); hermana = lo que diga \`python3 herramientas/hermanas.py <id>\` (el segundo campo, si no dice «sin hermana»). Devuelve el objeto items. No lances agentes ni uses git.`, { label: 'plan', phase: 'Plan', schema: PLAN, effort: 'low' })
const items = plan ? plan.items : []
log(`plan: ${items.map(i => `${i.id} (${i.modo})`).join(', ') || 'nada que hacer'}`)

const etapaReco = async (_, it) => {
  if (it.modo !== 'nueva') return { estado: 'sigue' }
  const r = await seguro(() => agent(`Serie ${it.id}.${hermana(it)}`, { label: `recolectar:${it.id}`, phase: 'Recolectar', schema: OK, agentType: 'recolector', effort: EF.aux }))
  if (!r) return { estado: 'cortada', donde: 'recolectar' }
  return { estado: 'sigue' }
}
const etapaInv = async (s, it) => {
  if (s.estado !== 'sigue') return s
  // nueva: los 4 roles; repaso: los 4 en modo repaso; repaso-corto: imagen, voz y texto (puntos 18-25); seguir: sólo lo que falte
  const roles = (it.modo === 'nueva' || it.modo === 'repaso') ? ROLES : it.modo === 'repaso-corto' ? ['imagen', 'voz', 'texto'] : [...new Set([...it.relanzar, ...it.faltan])]
  if (!roles.length) return s
  const modoDe = rol => it.modo === 'nueva' ? 'nueva' : (it.modo === 'repaso' || it.modo === 'repaso-corto') ? 'repaso' : (it.relanzar.includes(rol) ? 'seguir' : 'nueva')
  const nota = it.modo === 'repaso-corto' ? ' Repaso corto: sólo tus puntos de los 18-25, que son nuevos en el encargo y no están en la biblia; mira `python3 herramientas/seccion.py <id> --indice` para no repetir nada.' : ''
  const r1 = await parallel(roles.map(rol => () => seguro(() => agent(`Serie ${it.id}, modo ${modoDe(rol)}.${nota}${hermana(it)}`, { label: `inv:${it.id}:${rol}`, phase: 'Investigar', schema: INV, agentType: `investigador-${rol}`, effort: EF.inv }))))
  if (roles.some((_, i) => !r1[i])) return { ...s, estado: 'cortada', donde: `investigadores (${roles.filter((_, i) => !r1[i]).join(', ')})` }
  const pend = roles.filter((_, i) => r1[i].sigue_pendiente)
  if (pend.length) {
    log(`${it.id}: relanzo ${pend.join(', ')}`)
    const r2 = await parallel(pend.map(rol => () => seguro(() => agent(`Serie ${it.id}, modo relanzo.${hermana(it)}`, { label: `inv2:${it.id}:${rol}`, phase: 'Investigar', schema: INV, agentType: `investigador-${rol}`, effort: EF.inv }))))
    if (pend.some((_, i) => !r2[i])) return { ...s, estado: 'cortada', donde: 'relanzo' }
  }
  // medir las partes antes de pagar el redactor: lo flojo se relanza una vez más (modo seguir)
  if (it.modo !== 'repaso-corto') {
    const rp = await seguro(() => agent(`Serie ${it.id}. Roles: ${roles.join(', ')}.`, { label: `revisor-partes:${it.id}`, phase: 'Investigar', schema: FLOJAS, agentType: 'revisor-partes', effort: EF.aux }))
    const flojas = rp ? rp.flojas.filter(f => roles.includes(f.rol) && !pend.includes(f.rol)) : []
    if (flojas.length) {
      log(`${it.id}: partes flojas: ${flojas.map(f => `${f.rol} (${f.por_que || ''})`).join(', ')}; un relanzo`)
      const r3 = await parallel(flojas.map(f => () => seguro(() => agent(`Serie ${it.id}, modo seguir. Tu parte está floja según revisar_partes.py: ${f.por_que || 'corta'}. Completa lo obligatorio que falte de tus puntos, hasta 50 acciones.${hermana(it)}`, { label: `inv3:${it.id}:${f.rol}`, phase: 'Investigar', schema: INV, agentType: `investigador-${f.rol}`, effort: EF.inv }))))
      if (flojas.some((_, i) => !r3[i])) return { ...s, estado: 'cortada', donde: 'relanzo de partes flojas' }
    }
  }
  return { ...s, estado: 'sigue' }
}
const etapaRedactor = async (s, it) => {
  if (s.estado !== 'sigue') return s
  const modo = it.modo === 'repaso-corto' ? 'repaso-corto' : it.modo === 'repaso' ? 'repaso' : (it.biblia_existe ? 'seguir' : 'nueva')
  const r = await seguro(() => agent(`Serie ${it.id}, modo ${modo}.${hermana(it)}`, { label: `redactor:${it.id}`, phase: 'Redactar', schema: RED, agentType: 'redactor', effort: EF.red }))
  if (!r) return { ...s, estado: 'cortada', donde: 'redactor' }
  return { ...s, estado: 'cerrar', red: `${r.resumen}${r.avisos ? ' · AVISOS: ' + r.avisos : ''}` }
}
const cierre = (ultimo) => async (s, it) => {
  if (s.estado !== (ultimo ? 'cerrar2' : 'cerrar')) return s
  const r = await seguro(() => agent(`Serie ${it.id}, lote ${it.lote}.${ultimo ? ' Es el intento final.' : ''} Resumen y avisos del redactor: «${(s.red || '').replace(/`/g, "'").slice(0, 1500)}»`, { label: `${ultimo ? 'cierre2' : 'cierre'}:${it.id}`, phase: 'Cerrar', schema: CIERRE, agentType: 'cierre', effort: EF.aux }))
  if (!r) return { ...s, estado: 'cortada', donde: 'cierre' }
  if (r.completa && r.subido) { log(`${it.id}: COMPLETA y subida`); return { ...s, estado: 'completa' } }
  if (ultimo) { log(`${it.id}: se queda a medias (${r.falta})`); return { ...s, estado: 'a medias', falta: r.falta } }
  log(`${it.id}: falta ${r.falta}; un reparo del redactor`)
  return { ...s, estado: 'reparar', falta: r.falta }
}
const etapaReparo = async (s, it) => {
  if (s.estado !== 'reparar') return s
  const r = await seguro(() => agent(`Serie ${it.id}, modo reparo. Falta según revisar.py: «${s.falta}».${hermana(it)}`, { label: `reparo:${it.id}`, phase: 'Redactar', schema: RED, agentType: 'redactor', effort: EF.red }))
  if (!r) return { ...s, estado: 'cortada', donde: 'reparo' }
  return { ...s, estado: 'cerrar2', red: `${r.resumen}${r.avisos ? ' · AVISOS: ' + r.avisos : ''}` }
}

// redactar de 2 en 2 (sólo un Opus cada una); seguir y nuevas de 1 en 1 (hasta 4 Sonnet + 1 Opus)
const tandas = []
const red = items.filter(i => i.modo === 'redactar'), resto = items.filter(i => i.modo !== 'redactar')
for (let i = 0; i < red.length; i += 2) tandas.push(red.slice(i, i + 2))
for (const it of resto) tandas.push([it])
const resultado = { completas: [], a_medias: [], cortadas: [], no_lanzadas: [] }
let seguidas = 0
for (const tanda of tandas) {
  if (seguidas >= 2) { resultado.no_lanzadas.push(...tanda.map(i => i.id)); continue }
  const res = await pipeline(tanda, etapaReco, etapaInv, etapaRedactor, cierre(false), etapaReparo, cierre(true))
  tanda.forEach((it, k) => {
    const s = res[k]
    if (!s || s.estado === 'cortada') { resultado.cortadas.push(`${it.id} (${s ? s.donde : 'error'})`); seguidas++ }
    else if (s.estado === 'completa') { resultado.completas.push(it.id); seguidas = 0 }
    else { resultado.a_medias.push(`${it.id}: ${s.falta || s.estado}`); seguidas = 0 }
  })
  if (seguidas >= 2) log('dos series seguidas cortadas (¿límite de uso?): no lanzo más')
}
return resultado
