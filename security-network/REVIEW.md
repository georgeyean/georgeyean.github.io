# International security research, c. 2006–2026: where it went, what settled, what is open

A narrative companion to `graph.json` and `network.html` in this folder. The graph has 262 work nodes, 21 theme nodes and 283 typed relations. Each theme section follows the same order: **what was claimed → what the evidence settled → what is contested → gaps and research opportunities**. Node ids in brackets (e.g. `[fearon1995]`) point to entries in `graph.json`.

**How the works were chosen.** This map was built differently from the IPE one, to avoid leaning on one library.
- **83 works** come from your Zotero library (`papers.json`). Their claims are condensed from the repo's "Theory & evidence" analyses.
- **150 works** were selected from the 400 most-cited 2006–2026 articles in each of fifteen journals in Crossref: *IO, WP, APSR, AJPS, JOP, ISQ, BJPS, IS, Security Studies, JCR, JPR, JSS, CMPS, RIPE, RIO*. Their title, authors, year, venue and DOI come from Crossref records.
- **29 anchors** are books and pre-2006 classics that organize the debates (Schelling, Jervis, Waltz, Fearon's antecedents, Kalyvas, Fortna). Crossref confirmed 28; Waltz 1979 has no Crossref record.

One-line claims for non-repo works are my summaries and were not re-read this session. Civil war and terrorism dominate citation counts, so the map is denser there than in nuclear and alliance politics, where key work is often in books.

---

## 1. Bargaining theory and rationalist explanations for war

**Claimed.** Because war is costly, rational states should find a settlement. War needs a specific failure: private information with incentives to misrepresent, commitment problems, or indivisibility `[fearon1995]`. Large, rapid power shifts create commitment problems even with full information, and indivisibility reduces to commitment `[powell2006]`. If information is the cause, war onset is unpredictable case by case `[gartzke1999]`.

**Settled.** The bargaining framework is the field's common language. It travels to civil war settlement `[walter1997]`, terrorism `[kyddwalter2006]`, debt-financed mobilization `[slantchev2012]` and the costs of an armed peace `[leventoglu2007]`. Its core informational results survive changes in bargaining protocol `[feyramsay2010]`. Uncertainty about power shifts, not only their size, drives preventive war `[debsmonteiro2013]`.

**Contested.** Whether rationalist mechanisms explain real wars. Lake finds bargaining theory needs behavioral factors to explain Iraq `[lake2010]`, and Duelfer & Dyson trace the US–Iraq wars to chronic mutual misperception `[duelfer2011]`. Indivisibility is either a genuine rationalist cause `[toft2006]` or a social construction of legitimation strategies `[goddard2006]`, not reducible to commitment.

**Gaps and open questions.**
- *Measuring private information.* The framework's central variable is unobservable by design. Text-based measures of leaders' private assessments (declassified records, FRUS-style corpora, as in `[schub2022]`) could finally test information mechanisms directly. Validated LLM annotation makes such corpora codable at scale.
- *Bargaining with hierarchy and third parties.* `[beek2025]` models hierarchy and war jointly. Most bargaining models are still dyadic, while real crises (Taiwan, Ukraine) involve patrons, allies and economic coercers bargaining at once.
- *Economic tools inside the bargaining range.* Sanctions, export controls and supply-chain chokepoints change both sides' outside options before any shot is fired. The security bargaining literature rarely models them (see Section 18).

## 2. Audience costs, signaling and crisis diplomacy

**Claimed.** Leaders who back down after public threats pay domestic audience costs, so democracies can signal resolve credibly `[fearon1994]`. Opposition parties make those signals more informative `[schultz2001]`.

**Settled.** Citizens do disapprove of leaders who threaten and back down, at least in survey experiments `[tomz2007]`. Many autocracies also generate audience costs through elite audiences `[weeks2008]`, and Chinese citizens punish backing down too `[weissdafoe2019]`. The costs are real but conditional: they need a free press `[slantchev2006]`, shrink when leaders justify reversals or partisans are loyal `[levendusky2012]`, and split into inconsistency and belligerence components that different audiences weigh differently `[kertzerbrutger2015]`, `[trager2011]`.

**Contested.** Whether audience costs operate in real crises. Historical studies find leaders rarely created or feared them `[snyder2011]`, `[trachtenberg2012]`, and private threats can be efficient precisely because they avoid them `[kurizaki2007]`. The democratic credibility advantage disappears once real coercive threats are coded properly `[downes2012]`. Gender `[schwartzblair2020]`, leader attributes `[yarhimilo2018]` and issue area all condition the effect; for trade threats, economic self-interest overrides consistency `[casler2021]`.

**Gaps and open questions.**
- *Audience costs in autocracies under information control.* Quek & Johnston show Chinese leaders can de-escalate with face-saving tactics `[quek2018]`. How propaganda and censorship manage audience costs over a long rivalry, rather than one vignette, is open.
- *Economic coercion and audience costs.* Tariff and sanctions threats are now more common than military threats among great powers. A full audience-cost literature on economic threats (with economic losers as the audience) barely exists beyond `[casler2021]`.
- *Real-world measurement.* Leader speeches and state media are machine-readable. Commitment language and backing-down episodes could be coded across many crises, replacing the vignette with observational evidence.

## 3. Regime type, the democratic peace and autocratic conflict

**Claimed and settled.** The dyadic democratic peace survives most statistical critiques `[dafoe2011]`. Democratic publics are less willing to strike democracies, because they see them as less threatening and attacking them as immoral `[tomzweeks2013]`, and public opinion constrains democratic leaders' decisions `[tomz2020io]`. Autocracies differ sharply: personalist and military regimes initiate more conflicts than civilian machine regimes `[weeks2012]`. Leaders' post-tenure fates shape war choices `[debsgoemans2010]`, and revolutionary leaders are more belligerent `[colgan2013wp]`. Women's suffrage contributes to the democratic peace `[barnhart2020]`.

**Contested.** Competing explanations for peace among democracies: capitalism and shared interests `[gartzke2007]`, settled borders producing both democracy and peace `[gibler2007]`, and institutions rather than public preferences, since Chinese citizens share democratic publics' aversion `[bellquek2018]`.

**Gaps and open questions.**
- *Autocratic peace and autocratic alignment.* If civilian autocracies behave like democracies on conflict initiation `[weeks2012]`, is there a peace among institutionalized autocracies, and does it underpin an autocratic order (China, Russia, Iran, Gulf)? This connects directly to work on autocratic rise.
- *Democratic backsliding and conflict.* Most regime-type research codes stable types. How backsliding democracies, with weakened oppositions and media, behave in crises is untested.
- *Regime type and economic coercion.* Do democracies weaponize interdependence differently from autocracies, which use informal measures? The answer bridges this map and the IPE one.

## 4. Reputation, credibility and coercion

**Claimed.** Coercion works through threats whose credibility rests on commitment and reputation `[schelling1966]`. Two influential books argued reputations matter less than thought: adversaries attribute backing down to situations rather than character `[mercer1996]`, and leaders judge credibility by current power and interests `[press2005]`.

**Settled, roughly.** The pendulum swung back. Past behavior shapes how states are treated `[crescenzi2007]`, and states that backed down are challenged more often `[weisiger2015]`. Reputation costs depend on observers' dispositions `[brutgerkertzer2018]`, and resolve is partly a psychological trait `[kertzer2016]`. New leaders lack reputations and may fight to build them `[wolford2007]`.

**Contested.** Compellence versus deterrence. Strong challengers often fail to compel weak targets because compliance invites more demands `[sechser2010]`. Madman reputations aid deterrence but undermine compellence `[mcmanus2021]`. Leaders read intentions from vivid personal impressions rather than calculated capabilities `[yarhimilo2014]`.

**Gaps and open questions.**
- *Reputation across issue areas.* Does backing down on a trade or sanctions threat cost credibility on military commitments, and vice versa? The economic-coercion boom makes this testable.
- *Reputation in a networked world.* Reputations now form in real time on social media and in state media. How fast reputational information spreads, and to whom, is unstudied.

## 5. Nuclear weapons: deterrence, proliferation and escalation

**Claimed.** States pursue nuclear weapons for security, domestic coalitions or prestige `[sagan1996]`. Nuclear symmetry lowers the risk of war but raises low-level disputes `[rauchhaus2009]`.

**Settled.** Proliferation follows security threats and latent capacity and is dampened by the NPT and allies `[jogartzke2007]`. Peaceful nuclear cooperation raises proliferation risk `[fuhrmann2009]`. Nuclear weapons deter but rarely compel `[sechser2017]`. Posture matters: only asymmetric-escalation postures deter conventional attack `[narang2014]`. The US public shows little nuclear taboo `[press2013]`, `[saganvalentino2017]`.

**Contested.** Whether superiority matters `[kroenig2013]` or only resolve. Whether counterforce technology erodes survivable deterrence `[lieberpress2006]`, `[lieberpress2017]`. How big inadvertent US–China escalation risk is: entanglement raises it `[acton2018]`, China's mobile forces and centralized command lower it `[wu2022]`, and Chinese confidence that war stays conventional may itself be dangerous `[cunninghamfravel2019]`. China may substitute cyber, space and conventional missiles for nuclear leverage `[cunningham2020]`.

**Gaps and open questions.**
- *Three-party nuclear competition.* Deterrence theory is bipolar. US–Russia–China dynamics, with China's buildup, have little formal or empirical treatment.
- *Nonnuclear strategic weapons.* Conventional precision strike, counterspace and cyber blur the nuclear threshold. Escalation theory for these "strategic substitution" tools is underdeveloped.
- *Nonproliferation through institutions and intelligence.* `[carnegiecarson2019]` shows intelligence-sharing IOs deter violations. Export controls on dual-use nuclear and missile technology are a parallel tool that the security literature rarely connects to trade data. HS-6 dual-use classifications could measure latent-capacity diffusion directly.

## 6. Alliances, reassurance and extended deterrence

**Claimed.** States balance threats, not power `[walt1987]`. Allies face an abandonment-entrapment dilemma `[snyder1984]`. Defensive alliances deter challenges to members `[leeds2003]`.

**Settled.** Alliance reliability is endogenous to changing circumstances `[leedssavun2007]`, and reputations for reliability attract partners `[crescenzi2012]`. Formal alliance commitments deter attacks on protégés, while forward-deployed nuclear weapons add little `[fuhrmannsechser2014]`. US alliances rarely entrapped Washington `[beckley2015]`, partly because careful design limits entrapment `[kim2011]`, and their budget burden is modest `[alley2021]`.

**Contested.** Why the US built bilateral alliances in Asia: collective identity `[hemmer2002]` or control of risky allies `[cha2010]`. Whether NATO enlargement broke assurances to Moscow `[shifrinson2016]`, and whether it built or broke trust `[kydd2001]`. Patrons choose between arms transfers and alliances `[yarhimilo2016]`.

**Gaps and open questions.**
- *Alliances and economic security.* Allies now coordinate export controls, screening and supply chains. Whether economic coordination substitutes for or reinforces military commitments (as trade linkage once did `[poast2012]`) is open.
- *Hedging middle powers.* The alliance literature codes formal treaties. Partial alignment by Vietnam, India, the Gulf states and others needs a measure of degree, not presence.

## 7. Great-power competition, status and hierarchy

**Claimed.** Differential growth produces hegemonic war `[gilpin1981]`. Great powers maximize relative power `[mearsheimer2001]`.

**Settled.** Status is a real driver: states with status deficits initiate more disputes `[renshon2016]`, unipolarity dampens status competition `[wohlforth2009]`, and rising powers seek status through creativity and competition `[larson2010]`. Status contestation can start from below, with smaller states, before it reaches established powers `[lin2024]`. Narcissistic leaders seek prestigious opponents `[harden2021]`.

**Contested.** How big the US lead is: Brooks & Wohlforth and Beckley see a durable lead `[brookswohlforth2016]`, `[beckley2018]`. Whether US deep engagement pays `[brooks2013]` or persists through establishment habit `[porter2018]`, and how much primacy pays economically `[drezner2013]`. Whether the liberal order was bound to fail `[mearsheimer2019]`, and whether hegemonic orders are better studied as dynamic and contested `[ikenberrynexon2019]`. How secondary states behave under unipolarity `[walt2009]`, `[goh2008]`.

**Gaps and open questions.**
- *Order contestation measured.* Status and order debates rely on case studies and diplomatic-exchange networks. Lin's text corpus `[lin2024]` shows how official statements can measure status claims. Extending that to many states' discourse about order would give a standard measure of contestation, which fits your order-contestation work.
- *Hierarchy beyond the US.* China's and Russia's regional hierarchies (deference, basing, votes) are understudied with the tools of `[beek2025]` and `[goh2008]`.

## 8. US–China rivalry and the Western Pacific balance

**Claimed.** China was largely a status quo power in the 1990s `[johnston2003]`; theories split on whether conflict is inevitable `[friedberg2005]`. China compromised in most territorial disputes when facing internal threats `[fravel2008]`.

**Settled.** Security-dilemma dynamics are intensifying in the Asia-Pacific `[liff2014]`. China's strategy mixes reassurance, institutional reform and resistance `[goldstein2020]`. Southeast Asia shows competitive coexistence, not a clean power shift `[shambaugh2018]`. Anti-access capabilities already erode US power projection `[montgomery2014]`. Weapon complexity limits Chinese imitation of US technology `[gilli2019]`. The economic realm now shows security-dilemma dynamics too `[pearson2022]`.

**Contested.** Policy. A grand bargain over Taiwan `[glaser2015]` versus Taiwan's military value `[greentalmadge2022]`. How much risk to run in the South China Sea `[fravelglaser2022]`. Whether China can back down in crises `[quek2018]`, `[weissdafoe2019]`. Escalation risk, as Section 5 shows.

**Gaps and open questions.**
- *Economic statecraft inside the military rivalry.* Export controls, entity lists and Chinese counter-controls are now central to the balance, but security scholarship treats them as background. Linking dual-use trade flows to military capability assessments is a clear opening.
- *Third-country alignment.* How Southeast Asian, South Asian and Gulf states position themselves, measured continuously, is the dependent variable the field needs.
- *Domestic politics of Chinese security policy.* Repression in Xinjiang shifted to preventive mass detention `[greitens2020]`. How internal security priorities shape external behavior remains thinly studied quantitatively.

## 9. Leaders, psychology and elite decision-making

**Claimed and settled.** Misperception is systematic `[jervis1976]`, and psychology underlies rational models rather than only explaining error `[mercer2005]`. Leaders matter: beliefs shape intervention strategies `[saunders2011]`, military backgrounds predict militarized behavior `[horowitzstam2014]`, culpability shapes war duration `[croco2011]`, and experience shapes how advisers' biases aggregate `[saunders2017]`. Bureaucratic position shapes the advice leaders get `[schub2022]`.

**Contested.** How much social science informs practitioners: little for security officials compared with trade and development officials `[avey2022]`. Whether women executives raise conflict behavior `[koch2011]`.

**Gaps.** Leader-level data stop at background traits. Text of leaders' own words in many countries could measure beliefs, risk attitudes and status concerns systematically, beyond the US-focused archives.

## 10. Public opinion, casualties and the use of force

**Claimed and settled.** Casualty tolerance depends on expected success `[gelpi2006]`, casualty trends `[gartner2008]` and media coverage `[fetzer2025]`. Local casualties cost incumbents votes `[karol2007]`. International endorsement acts as a second opinion `[grieco2011]`.

**Contested.** Elite cues and partisanship versus events `[berinsky2007]`. Group identity shapes support, as with the Black-white gap `[greenriley2023]`. Legal information lowers support for drone strikes even when they work `[kreps2016]`. Terror threats shift voters right `[berrebi2008]`, `[getmansky2014]`, `[giavazzi2024]`.

**Gaps.** Public opinion research focuses on US and Israeli publics and on military force. Publics in allied and third countries, and their views of economic coercion and decoupling, are thinly studied.

## 11. Territory, borders and indivisibility

**Claimed and settled.** Territory is unusually conflict-prone `[johnsontoft2014]`. Settled borders produce peace and democracy `[gibler2007]`. Borders that follow prior administrative lines are more peaceful `[cartergoemans2011]`. Leaders use territorial disputes for diversion `[tir2010]`. Resource-rich territory raises domestic distributive conflict, so states claim it less `[lee2024]`. Globalized production lowers the benefits of conquest `[brooks1999]`.

**Gap.** Border fortification is a state-building project with a corruption trade-off `[blair2025]`. The global rise of walls and fences has security, trade and migration effects that are rarely studied together.

## 12. Civil war onset: state capacity, ethnicity and grievance

**Claimed.** Opportunity, not grievance, predicts civil war `[collier2004]`. Onset follows conditions favoring insurgency, such as weak states and rough terrain `[fearonlaitin2003]`.

**Settled.** Few onset correlates are robust `[hegresambanis2006]`. Ethnic exclusion from state power predicts rebellion `[cedermangirardin2007]`, `[cederman2010]`. Horizontal economic inequalities between groups matter, reviving grievance `[cederman2011]`. State capacity is best measured by bureaucratic and fiscal quality `[hendrix2010]`. Refugee flows spread civil war `[salehyan2006]`, and the international system shapes the technology of rebellion `[kalyvasbalcells2010]`.

**Contested.** Climate: rainfall shocks raise social conflict `[hendrixsalehyan2012]` but drought shows little robust effect on civil war `[theisen2012]`. Resource location matters `[lujala2010]`. The regime–civil war link is partly a coding artifact `[vreeland2008]`. Coup-proofing by exclusion produces civil war `[roessler2011]`.

**Gaps.** Prediction now combines structural risk with behavioral triggers `[gibler2016]`. Text-based early warning from news and NGO reports, coded by validated LLMs, could greatly expand trigger data.

## 13. Civil war dynamics, rebel organization and violence against civilians

**Claimed.** Selective violence follows territorial control `[kalyvas2006]`. Rebel organization and resource endowments shape abuse `[weinstein2007]`.

**Settled.** Both grievance and selective incentives explain who fights `[humphreysweinstein2008]`. Organization and recruitment shape abuse of civilians `[humphreysweinstein2006]`. Weak rebels kill more civilians `[wood2010]`. External sponsors shape rebel behavior `[salehyan2011]`, `[salehyan2014]`. Rebels build wartime institutions `[arjona2014]` and govern for state-making `[stewart2018]`. Recruitment by abduction drives wartime rape `[cohen2013apsr]`, `[cohen2013wp]`. Nonviolent campaigns succeed more often `[stephanchenoweth2008]`.

**Contested.** Indiscriminate violence: it reduced insurgent attacks in Chechnya `[lyall2009]` but backfired in Vietnam `[kocher2011]`, and repression's effects are non-monotonic `[zhukov2023]`. Mechanized militaries lose counterinsurgencies `[lyallwilson2009]`. Civilians punish foreign forces more than insurgents for harm `[lyall2013]`.

**Gap.** Micro-level civil war research is dense in a few cases (Sierra Leone, Uganda, Colombia, Afghanistan, Chechnya). Cross-case integration of micro findings, and the effects of new technologies (drones, phones, social media) on rebel control, need attention.

## 14. War termination, peacekeeping and intervention

**Claimed and settled.** Civil wars rarely end in settlement because sides cannot commit to disarm; third-party guarantees help `[walter1997]`. Peacekeeping works, once selection into hard cases is addressed `[fortna2004]`, `[fortna2008]`. UN troops protect civilians `[hultman2013]`, reduce battle deaths `[hultman2014]` and work locally `[fjelde2019]`, `[ruggeri2017]`. Agreement design that eases commitment problems lasts `[mattes2009]`. Foreign-imposed regime change prolongs interstate peace `[lo2008]`.

**Contested.** Rebel victory produces more durable peace than settlement `[toft2010]`. Mediation yields agreements without peace `[beardsley2008]`. Expected intervention creates moral hazard for rebels `[kuperman2008]`. Active ICC involvement prolongs wars `[prorok2017]`. Governments fight separatists to deter others `[walter2006]`.

**Gap.** UN peacekeeping is shrinking while ad hoc and regional missions and private military companies grow. Evidence on whether these alternatives work comparably is thin.

## 15. Terrorism and counterterrorism

**Claimed.** Terrorism is costly signaling with five strategies `[kyddwalter2006]`. Terrorists provoke repression to mobilize supporters `[bdmdickson2007]`.

**Settled.** Terrorism rarely achieves its political goals `[abrahms2006]` and hurts rebels' civil war outcomes `[fortna2015]`. Failed states host more transnational terrorism `[piazza2008]`. Larger, religious and well-connected groups are deadlier `[asal2008]`. Weak leadership control leads to more civilian targeting `[abrahms2015]`.

**Contested.** Decapitation helps counterinsurgency `[johnston2012]` but bureaucratized groups survive it `[jordan2014]`. Drone strikes reduced militant violence in Pakistan `[johnstonsarbahi2016]`. Democratic competition encourages terrorism through outbidding `[chenoweth2010]`. Gender norms shape the lethality of female attackers `[thomas2021]`.

**Gap.** The post-ISIS decline of transnational jihadist terrorism and the rise of far-right and lone-actor violence in democracies have not been integrated into the strategic theories built on 2000s data.

## 16. Military power, technology, cyber and AI

**Claimed.** Force employment explains battlefield outcomes better than material preponderance `[biddle2004]`. Military innovations diffuse according to financial and organizational demands `[horowitz2010]`.

**Settled.** Cyber operations are sabotage, espionage and subversion rather than war `[rid2012]` and cannot substitute for force `[gartzke2013]`. They favor strong states `[lindsay2013]` and barely moved battlefield events in Ukraine `[kostyukzhukov2019]`. Attribution is a political process `[ridbuchanan2015]`. The cyber offense-defense balance depends on organizational skill and cost `[slayton2017]`.

**Contested.** Whether cyber is revolutionary for statecraft `[kello2013]`. Whether cyber deterrence and coercion can work `[nye2017]`, `[borghard2017]`. Whether AI and autonomy speed war beyond human control `[horowitz2019jss]` or make human judgment more important `[goldfarb2022]`.

**Gaps.** The Ukraine war (drones, commercial satellites, electronic warfare) is a large natural experiment whose systematic analysis is just starting. The economic base of military technology, through semiconductors, dual-use supply chains and export controls, is where security and IPE meet most directly. Your HS-6 dual-use classification is a direct measurement tool here.

## 17. Institutions, laws of war and international courts

**Claimed and settled.** Ratification creates reciprocal compliance with the laws of war, especially among democracies `[morrow2007]`. The ICC deters atrocity by governments and legitimacy-seeking rebels `[josimmons2016]`, and prosecutions reduce repression `[kimsikkink2010]`. Coercers seek Security Council approval to transmit information `[thompson2006]`. Generalized trust enables binding security institutions `[rathbun2011]`.

**Contested.** Realists doubt institutions' independent effect `[mearsheimer1994]`. ICC involvement can prolong wars `[prorok2017]`. Advocacy gatekeepers shape which weapons become norm campaigns `[carpenter2011]`.

**Gap.** The arms-control architecture is eroding (INF, New START, Open Skies). Why regimes collapse, and whether informal or technical arrangements can replace them, has little systematic research.

## 18. Economics of security: resources, interdependence and finance

**Claimed and settled.** Oil causes international conflict through many pathways `[colgan2013]`, though only specific mechanisms matter for US security `[glaser2013]`. China's energy mercantilism buys real security `[lindpress2018]`. Trade promotes peace in simultaneous estimates `[hegre2010]`. Credit access shapes alliances `[allen2013]` and war `[slantchev2012]`. Military spending tracks the threat environment `[nordhaus2012]`.

**Contested.** Whether interdependence pacifies or becomes a weapon. Network hubs can be weaponized `[farrellnewman2019]`, and party-state capitalism turns firms into perceived capabilities `[pearson2022]`. Relative gains matter only when gains cumulate `[matthews1996]`.

**Gaps.** This is the bridge to the IPE map, and the opening is large.
- Security work treats economic statecraft as context. IPE treats military consequences as context.
- A joint measurement program would connect them: dual-use trade exposure, export-control coverage, defense-industrial dependence and alliance ties in one panel.

## 19. Gender, war and political violence

Women's physical security predicts state peacefulness `[hudson2009]`. War lowers women's life expectancy more than men's `[plumper2006]`. Suffrage contributes to the democratic peace `[barnhart2020]`, while women executives may act more hawkishly `[koch2011]`. Gender stereotypes shape audience costs `[schwartzblair2020]` and terrorist effectiveness `[thomas2021]`, and women also perpetrate wartime rape `[cohen2013wp]`.

**Gap.** The selection of women leaders in competitive contexts confounds the executive-hawkishness finding. Designs that separate selection from effect are needed.

## 20. Coups, repression and internal security

Coups declined after the Cold War but persist in Africa `[powellthyne2011]`. Dictators who rely on the military must share power with it `[svolik2012]`, and power sharing trades coup risk for rebellion risk `[paine2021]`, `[roessler2011]`. Protest helps coup plotters coordinate `[caspertyson2014]`. Democracy reduces repression mainly through voice `[davenport2007]`, and judicial independence is among the strongest predictors `[hilljones2014]`. Repression's effects depend on intensity and credibility `[rozenaszhukov2019]`, `[zhukov2023]`.

**Gap.** Digital repression (surveillance, internet shutdowns, AI-enabled monitoring) and its export by China and others links internal security to international technology markets. It is barely studied as a trade and security question together.

## 21. IR theory: realism, constructivism and cooperation

The map's theoretical base: anarchy and the distribution of power `[waltz1979]`, which constructivists answered by arguing anarchy is what states make of it `[wendt1992]`; the offense-defense security dilemma `[jervis1978]`; cooperation among egoists `[axelrod1981]` and its limits in security `[lipson1984]`; practices that sustain security communities `[pouliot2008]`; and critiques of balance-of-power theory `[nexon2009]`. Bargaining theory (Section 1) has largely replaced structural realism as the working framework in top journals, while realism survives mainly in grand-strategy debates (Section 7).

---

## Cross-cutting roadmap: where your work fits

1. **Economic statecraft inside security bargaining.** Sections 1, 2, 5, 8 and 18 all leave economic coercion outside the model. A bargaining model or empirical design treating export controls and sanctions as moves in crisis bargaining, with audience costs for economic threats, is open ground. *Asset:* the HS-6 dual-use classification as a measure of what is being withheld.
2. **Measuring order contestation and alignment.** Status, hierarchy and alignment research (Sections 6, 7 and 8) lacks a continuous, cross-national measure of where states stand between competing orders. *Asset:* LLM annotation of official statements, building on `[lin2024]`.
3. **Autocratic security cooperation.** Sections 3, 12 and 20 show autocracies differ internally but say little about how autocracies cooperate in security (arms transfers, repression technology, mutual protection). This connects to autocratic rise and to the autocratic-IFI work in the IPE map.
4. **Text as data for unobservables.** Private information, resolve, status concerns and threat perception are central but unmeasured. Validated LLM coding of archives, speeches and state media is the enabling method.

## What I could not verify (flagged)

- **Anchors:** 28 of 29 confirmed in Crossref, books often through reviews or reprint DOIs. Waltz 1979 has no Crossref record.
- **Library entries:** several had PDF file names or missing authors in `papers.json` (Beckley 2018, Montgomery 2014, Brooks, Ikenberry & Wohlforth 2013, van Beek et al., Lin, Lee, Blair, Fetzer et al., Giavazzi et al.). I corrected them from Crossref. Mukaigawara's *AJPS* article could not be found in Crossref, so its 2025 date is assumed.
- **Dates:** Crossref uses online-first dates for some articles, so a few show a year earlier than print (for example Cederman et al. 2009 for the 2010 *World Politics* issue). Cunningham's "Strategic Substitution" is 2022, not 2020.
- **Claims:** one-line claims and edge justifications for the 179 non-library works are my summaries, not checked against full text this session.
- **Coverage:** citation counts favor civil war and terrorism datasets and older work. Nuclear, alliance and grand-strategy scholarship is more book-based and so is represented mainly through anchors. Work from 2023–2026 is under-sampled.
