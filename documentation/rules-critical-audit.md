# Sonos Rules Critical Perspective Audit

Date: 2026-05-10
Status: first-pass design audit
Method: `critical-perspective` applied to modular rules + local ontology

## Inputs Read

- `infranodus/rules-ontology.md`
- `vaults/system/rules/index.md`
- `vaults/system/rules/core/checks-de-habilidades-en-rol.md`
- `vaults/system/rules/character/atributos-de-un-cantor.md`
- `vaults/system/rules/character/vitalidad.md`
- `vaults/system/rules/character/silencio.md`
- `vaults/system/rules/character/resonancia.md`
- `vaults/system/rules/character/auralium.md`
- `vaults/system/rules/instrument/dano-de-un-instrumento-vital.md`
- `vaults/system/rules/instrument/pulsos.md`
- `vaults/system/rules/instrument/rudimentos.md`
- `vaults/system/rules/instrument/fundamentos.md`
- `vaults/system/rules/instrument/mejoras-del-instrumento-vital.md`
- `vaults/system/rules/instrument/desafinacion.md`
- `vaults/system/rules/combat/iniciativa.md`
- `vaults/system/rules/combat/acciones-por-turno.md`
- `vaults/system/rules/combat/movimiento.md`
- `vaults/system/rules/combat/tension.md`
- `vaults/system/rules/combat/subidas-de-tension.md`
- `vaults/system/rules/combat/bajada-de-tension.md`
- `vaults/system/rules/combat/efectos-de-la-tension.md`
- `vaults/system/rules/combat/estados-negativos.md`
- `vaults/system/rules/combat/estados-positivos.md`
- `vaults/system/rules/negotiation/estadisticas-de-negociacion.md`
- `vaults/system/rules/negotiation/actitud-inicial-del-pnj.md`
- `vaults/system/rules/negotiation/hacer-argumentos.md`
- `vaults/system/rules/negotiation/oferta-del-pnj.md`
- `vaults/system/rules/negotiation/motivaciones-y-escollos.md`

## Executive Summary

The current rules have a strong musical identity and several promising engines: `Resonancia` as momentum, `Silencio` as defense/counterplay, `Tensión` as global pressure, and `Instrumento Vital` as the core character expression layer.

The main critical issue is not that the mechanics are weak. It is that several mechanics currently carry multiple jobs at once without enough procedure around edge cases. This can create ambiguity for AI assistants, DMs, and players.

Highest-priority design questions:

1. Is `Silencio` meant to be only damage reduction, or also a parry/counterattack engine and Resonancia battery?
2. Is `Tensión` meant to be danger, comeback mechanic, encounter timer, or all three?
3. Are `Rudimentos` and `Fundamentos` balanced by action economy, Resonancia, equip slots, evolution, or all of those simultaneously?
4. Should `Desafinación` be a temporary penalty pool, a corruption track, or an instrument condition system?
5. How much of `Negociación` is a closed minigame versus a framework for adjudicating roleplay?

## 1. Overloaded Concepts

### 1.1 Silencio

**Observed rule role:**

- Reduces incoming damage.
- Can completely block damage on `Silencio Perfecto`.
- Can turn incoming parity into `Parry` and return damage as true damage.
- Can recover `Resonancia` through `Silencio Perfecto`.
- Is doubled by `Defenderse`.
- Interacts with `On Garde`.
- Is disabled or modified by states such as `Condena` and `Maldecido`.

**Critical perspective:**

`Silencio` is doing at least four things: armor, saving throw, counterattack trigger, and resource engine. That can be exciting, but it makes defense potentially more rewarding than offense if not tightly bounded.

**Risk:**

A defensive build may generate more tempo than intended: block damage, recover Resonancia, trigger parries, then spend recovered Resonancia on Rudimentos.

**Question for design:**

Should perfect defense be a rare dramatic moment, or a build-around loop?

**Suggested clarification:**

Add a short rule section: `Silencio Timing and Limits`, answering:

- When exactly is Silencio rolled?
- Does it apply before or after resistances/vulnerability?
- Can a single attack trigger both `Silencio Perfecto` and `Parry`?
- Can `On Garde` stack with normal `Parry`?
- Is Resonancia recovery from Silencio limited per round?

References:

- `vaults/system/rules/character/silencio.md`
- `vaults/system/rules/character/resonancia.md`
- `vaults/system/rules/combat/acciones-por-turno.md`
- `vaults/system/rules/combat/estados-negativos.md`

### 1.2 Tensión

**Observed rule role:**

- Global combat pressure from 0 to 10.
- Goes up from end of round, enemy crits, player pifias, Cantor hitting 0 HP.
- Goes down from enemy pifias, player crits, `Afinar`, and `Resolver`.
- Gives both negative and positive effects at thresholds.
- At high values, strongly changes Resonancia, enemy damage, On Garde, counterattacks, and true damage.

**Critical perspective:**

`Tensión` is framed as pressure, but its table also grants powerful player benefits. This creates an interesting push-pull, but the intent is ambiguous: should players fear high Tensión, exploit it, or dance around it?

**Risk:**

Players may intentionally increase Tensión to access free/reduced Rudiments, passive On Garde, or stronger counterattack patterns.

**Question for design:**

Is Tensión a punishment clock or a volatility dial?

**Suggested clarification:**

Add a design note to `Tensión`:

- Low Tensión = stable combat?
- Mid Tensión = risk/reward?
- High Tensión = desperate chaos?
- Are player benefits at high Tensión intentional comeback tools?

Also define if threshold effects are cumulative or only current-tier effects.

References:

- `vaults/system/rules/combat/tension.md`
- `vaults/system/rules/combat/subidas-de-tension.md`
- `vaults/system/rules/combat/bajada-de-tension.md`
- `vaults/system/rules/combat/efectos-de-la-tension.md`

### 1.3 Resonancia

**Observed rule role:**

- Pays for `Rudimentos`.
- Starts at half maximum at combat start.
- Recovers from kills, perfect defense, Pulsos, and Meditar.
- Can be modified by states and Tensión.

**Critical perspective:**

`Resonancia` looks like the main pacing resource, but there are many ways to recover it. The system may incentivize alternating `Pulso` and `Rudimento`, which is likely intended, but the relative value of `Pulso`, `Meditar`, and defensive recovery needs watching.

**Risk:**

If Pulso both deals damage and recovers Resonancia, `Meditar` may only be attractive when attacking is impossible or unsafe. If Silencio Perfecto also recovers Resonancia, defensive loops may outcompete Meditar.

**Question for design:**

What is the intended default rhythm: Pulso → Rudimento, defend → counter, or spend/recover opportunistically?

**Suggested clarification:**

Add a small `Resonancia Economy` note:

- expected Resonancia gained per round;
- whether recovery can exceed maximum;
- whether multiple recovery triggers can happen in one turn/round;
- what role `Meditar` should fill compared to `Pulso`.

References:

- `vaults/system/rules/character/resonancia.md`
- `vaults/system/rules/instrument/pulsos.md`
- `vaults/system/rules/instrument/rudimentos.md`
- `vaults/system/rules/combat/acciones-por-turno.md`

## 2. Missing or Thin Procedures

### 2.1 Combat timing stack

The combat rules define actions and resources, but not a full timing order for attack resolution.

Missing sequence likely needed:

1. Choose action.
2. Choose target.
3. Pay PA / Resonancia.
4. Roll attack or effect, if any.
5. Calculate base damage.
6. Apply range modifiers.
7. Apply states, buffs, vulnerability/resistance.
8. Roll/apply Silencio.
9. Check Chirrido / Silencio Perfecto / Parry / On Garde.
10. Apply damage.
11. Check 0 Vitalidad / form change / unconsciousness.
12. Apply Tensión changes.

Without this, many interactions will need ad hoc rulings.

References:

- `vaults/system/rules/combat/acciones-por-turno.md`
- `vaults/system/rules/character/silencio.md`
- `vaults/system/rules/character/vitalidad.md`
- `vaults/system/rules/instrument/pulsos.md`

### 2.2 Damage taxonomy

The rules mention normal damage, true damage, damage from Pulso, Rudimentos, poison, Herido, enemy damage, and Instrument damage, but there is no single taxonomy of damage types and mitigation order.

Critical question:

Does `daño verdadero` ignore only Silencio, or also resistance, Escudo, and other reductions?

References:

- `vaults/system/rules/instrument/dano-de-un-instrumento-vital.md`
- `vaults/system/rules/character/silencio.md`
- `vaults/system/rules/combat/estados-negativos.md`
- `vaults/system/rules/combat/estados-positivos.md`

### 2.3 States need duration and stacking rules

The state lists are evocative and useful, but many entries use `X`, `N`, `próximo`, or broad language without default duration/stacking rules.

Examples:

- `Arritmia`: siguientes N tiradas.
- `Envenenado`: Xd6, reduce X each round.
- `Vulnerable`: damage increases by X.
- `Furia`: damage increases by X.
- `Escudo`: absorbs next X damage.
- `Flujo`: costs 1 less Resonancia.

Critical questions:

- Who defines X/N?
- Can the same state stack?
- Does reapplying refresh, add, or replace?
- Are states removed at end of combat?

References:

- `vaults/system/rules/combat/estados-negativos.md`
- `vaults/system/rules/combat/estados-positivos.md`

### 2.4 Instrument improvement risk loop

The upgrade system is promising, but `Desafinación` and corrupt improvements may need stronger consequence boundaries.

Observed:

- Failed/partial upgrades can add Desafinación.
- Desafinación subtracts dice from future rolls, one die at a time.
- Purification can remove all Desafinación for 2 Auralita Refinada.

Critical perspective:

If purification is cheap compared to upgrade costs, Desafinación may become a minor tax rather than a meaningful risk. If it is not cheap in campaign economy, it may be punishing. The current rules do not reveal the intended economy.

Question:

Should corrupt improvement be a tempting danger or mostly a resource optimization puzzle?

References:

- `vaults/system/rules/instrument/mejoras-del-instrumento-vital.md`
- `vaults/system/rules/instrument/desafinacion.md`

## 3. Possible Incentive Problems

### 3.1 Always-player-first initiative

Players always act first unless the DM says otherwise.

This supports planning and teamwork, but it has strong tactical consequences:

- alpha strikes are encouraged;
- enemy threat may need inflated HP or reactions;
- `Tensión` may need to compensate for player tempo advantage;
- encounter design may rely on enemy durability rather than initiative uncertainty.

Question:

Is the intended fantasy “the band acts together first,” or is this just a simplification?

References:

- `vaults/system/rules/combat/iniciativa.md`

### 3.2 Pulso may dominate Meditar

`Pulso` costs 1 PA, deals damage, and recovers 1 Resonancia. `Meditar` costs 2 PA and recovers 1dAT Resonancia.

This may be fine if `1dAT` is usually much better than 1, but the rules do not define `AT` clearly in the local module set.

Question:

When should a rational player choose Meditar over Pulso?

References:

- `vaults/system/rules/combat/acciones-por-turno.md`
- `vaults/system/rules/character/resonancia.md`
- `vaults/system/rules/instrument/pulsos.md`

### 3.3 Tensión benefits may incentivize risky play

At Tensión 3/4, first Rudiment cost reductions are very strong. At 6-7 and 8-9, passive defensive/counter mechanics appear. This may incentivize players to allow or cause Tensión increases.

Question:

Do you want players to manage Tensión like a dangerous musical crescendo, or prevent it like a doom clock?

References:

- `vaults/system/rules/combat/efectos-de-la-tension.md`

## 4. Negotiation System Observations

The negotiation rules have a strong skeleton: `Interés`, `Paciencia`, `Motivaciones`, `Escollos`, attitude, argument outcomes, offer table.

The main gap is not concept but procedure.

Needs clarification:

- What roll is made for an argument?
- Which skill applies?
- How does a success change Interés/Paciencia?
- How does failure change Interés/Paciencia?
- Are offers made after every argument even on failure?
- Can players discover Motivaciones/Escollos mechanically?
- Can multiple PCs argue in one negotiation round?

Critical question:

Is negotiation meant to be a tactical social minigame, or a light structure for DM judgment?

References:

- `vaults/system/rules/negotiation/estadisticas-de-negociacion.md`
- `vaults/system/rules/negotiation/actitud-inicial-del-pnj.md`
- `vaults/system/rules/negotiation/hacer-argumentos.md`
- `vaults/system/rules/negotiation/oferta-del-pnj.md`

## 5. AI / Pi Workflow Findings

The modular split is already useful. The critical-perspective pass suggests some future AI-facing modules that would improve both human rules quality and AI answers:

Recommended new/expanded modules in the master rules:

1. `Combat Resolution Timing`
2. `Damage Types and Mitigation Order`
3. `Resonancia Economy`
4. `Silencio Timing and Limits`
5. `Tensión Design Intent and Threshold Rules`
6. `State Duration, Stacking, and Removal`
7. `Negotiation Procedure`
8. `Instrument Improvement Economy`

These do not need to replace existing rules. They can be short procedural sections that make interactions unambiguous.

## 6. Priority Questions for Alberto

Answering these would remove many ambiguities:

1. Can one attack trigger both `Silencio Perfecto` and `Parry`?
2. Does `daño verdadero` ignore Silencio, resistance, Escudo, or all mitigation?
3. Are Tensión threshold effects cumulative?
4. Is high Tensión meant to be exploitable by players?
5. Can Resonancia recovery trigger multiple times per round?
6. What exactly is `1dAT` in Meditar?
7. What is the default duration/stacking rule for states?
8. How are X and N chosen for states?
9. What roll resolves a negotiation argument?
10. How expensive is 2 Auralita Refinada in campaign terms?

## 7. Suggested Next Actions

### Immediate

- Add a `Combat Resolution Timing` section to `vaults/system/rules.md`.
- Add a `State Rules` subsection before the positive/negative state tables.
- Add a `Negotiation Procedure` subsection after `Hacer Argumentos`.

### Medium-term

- Create a `sonos-balance-auditor` skill that reads the modular rules, cards, and this audit.
- Extend `infranodus/rules-ontology.md` with new relations after the missing procedures are written.

### Optional

- Add design-intent notes to generated modules or source rules, e.g. “Tensión is intended as a volatility dial, not only a punishment clock.”
