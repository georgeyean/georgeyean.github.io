# Comparative Politics, c. 1959–2026: where it went, what settled, what is open

A narrative companion to `graph.json` and `network.html` in this folder. The graph has 259 work nodes, 18 theme nodes and 251 typed relations. Each theme section follows the same order: **what was claimed → what the evidence settled → what is contested → gaps and research opportunities**. Node ids in brackets (e.g. `[gandhiprzeworski2007]`) point to entries in `graph.json`.

**How the works were chosen.**
- **Your library:** comparative papers from `papers.json`, mostly your *Gov Cp*, *Globalization*, *Research* and China groups. Claims are condensed from the repo's analyses.
- **Shared works:** works that also appear in the IPE, security or IR maps (Weeks, Svolik, Roessler, Norris & Inglehart, Fearon & Laitin) are imported unchanged.
- **Top-cited articles:** 154 come from the 400 most-cited 2006–2026 articles in 21 journals, including six comparative journals added for this map: *Comparative Political Studies*, *Comparative Politics*, *Journal of Democracy*, *EJPR*, *SCID* and the *Annual Review of Political Science*. I left out American politics and pure methods papers.
- **Anchors:** classic books and articles (Lipset, Moore, Dahl, Huntington, Boix, Acemoglu & Robinson, Esping-Andersen, Hall & Soskice, Levitsky & Way, Svolik). All new anchors were found in Crossref.

One-line claims for non-library works are my summaries and were not re-read this session.

---

## 1. Democratization and regime change

**Claimed.** Development makes democracy likely and durable `[lipset1959]`. Paths to democracy depend on class coalitions `[moore1966]`, mobilization needs institutions `[huntington1968]`, and transitions start with elite splits and pacts `[odonnell1986]` in international waves `[huntington1991]`.

**Settled, partly.** The development-democracy correlation is real. Whether development causes transitions or only sustains democracies is still disputed:
- it only sustains them `[przeworski1997]`;
- it also causes transitions `[boixstokes2003]`, `[epstein2006]`.

Distributive theories formalized the mechanism `[boix2003]`, `[acemoglurobinson2006]`. Selection explains why the fastest growers are autocracies `[luoprzeworski2019]`. Measurement matured from dichotomies `[boixmillerrosato2013]` to latent and multidimensional measures `[treierjackman2008]`, `[lindberg2014]`.

**Contested.** Inequality's role:
- inequality affects consolidation, not transitions `[houle2009]`;
- most transitions are not distributive at all `[haggardkaufman2012]`;
- rising middle classes demand democracy to protect property `[ansellsamuels2010]`.

International linkage and leverage `[levitskyway2006]`, missionary legacies `[woodberry2012]` and financial openness `[freeman2012]` add channels beyond domestic class conflict.

**Gaps.** Distributive theories were built on the 19th and 20th centuries. Whether they explain the current lack of new transitions, where autocracies are rich and integrated (the Gulf, China), is open. This connects to work on autocratic rise.

## 2. Democratic backsliding, polarization and support for democracy

**Claimed.** Backsliding now proceeds by executive aggrandizement rather than coups `[bermeo2016]`. Norm erosion and failed party gatekeeping kill democracies `[levitskyziblatt2018]`.

**Settled.** Polarization is the key enabler: partisans tolerate violations by their own side `[svolik2019]`, `[grahamsvolik2020]`, and affective polarization is high in Europe too `[reiljan2020]`. Backsliding follows a recognizable sequence `[haggardkaufman2021]` and produces new competitive authoritarian regimes `[levitskyway2020]`.

**Contested.** Whether democratic support is declining `[foamounk2016]`, `[foamounk2017]` or whether talk of a democratic recession `[diamond2015]` is overstated `[levitskyway2015]`. Economic crises reduce support `[armingeon2014]`. Theories remain fragmented `[waldnerlust2018]`.

**Gaps.**
- *International drivers of backsliding.* Most work is domestic. Autocratic external support (media, finance, regional organizations; see Section 3 and the IR map) is rarely modeled as a cause of backsliding.
- *Measuring aggrandizement in text.* Legislative and judicial changes that concentrate power are codable from legal texts and news with validated LLM annotation, which would date backsliding more precisely than expert surveys.

## 3. Authoritarian institutions and regime survival

**Claimed.** Regime types break down differently `[geddes1999]`, `[gwf2014]`. Institutions such as legislatures and parties co-opt opposition `[gandhiprzeworski2007]`, `[gandhi2008]` and make elite power sharing credible `[magaloni2008]`, `[boixsvolik2013]`. Authoritarian politics turns on two problems, power sharing and control `[svolik2012book]`.

**Settled.** Party-based regimes are the most durable `[magalonikricheli2010]`. Authoritarian elections serve co-optation and information `[gandhilust2009]`, and hegemonic parties survive by signaling invincibility `[magaloni2006]`. Legislatures raise investment `[wright2008]`. Coup-proofing by ethnic exclusion trades coups for civil war `[roessler2011]`, `[paine2021]`. Unearned income prolongs survival `[morrison2009]`, `[ahmed2012]`.

**Contested.** Whether hybrid regimes are unstable `[brownlee2009]`, `[levitskyway2010]`. What decides uprisings: the coercive apparatus `[bellin2012]` or opposition coalitions `[howardroessler2006]`. External sources of resilience include investment treaties `[arias2018]` and regional organizations `[debre2021]`.

**Gaps.** Authoritarian institutions research grew from Cold War-era data. The current generation of autocracies is wealthy, technologically sophisticated and internationally connected. Whether institutions still matter as much when digital surveillance and external finance substitute for co-optation is the obvious open question.

## 4. Censorship, propaganda and information in autocracies

**Settled.** Chinese censorship targets collective action, not criticism `[kingpanroberts2013]`. The state fabricates posts to distract `[king2017]` and tolerates some watchdog reporting to monitor officials `[lorentzen2014]`. Commercialized media make propaganda more persuasive `[stockmann2011]`. Russian state TV manipulates attribution rather than facts `[rozenasstukal2019]`. Resource-poor dictators allow freer media `[egorov2009]`. Transparency destabilizes autocracies `[hollyer2018]`.

**Contested.** Whether technology liberates `[diamond2010]` or controls `[king2017]`. Information problems in hierarchies cut both ways: local officials manipulate statistics `[wallace2014]` and conceal grievances `[panchen2018]`.

**Gaps.** Generative AI changes the economics of propaganda and censorship. No top-journal study yet measures autocratic use of LLMs for content production or moderation. External propaganda effects are also new territory `[mattingly2025]`.

## 5. Chinese politics: cadres, responsiveness and governance

**Claimed.** Decentralization and promotion tournaments drove China's growth `[montinola1995]`, `[lizhou2005]`, `[xu2011]`, with experimentation under hierarchy `[heilmann2008]`.

**Settled, partly.** Promotion depends on factional ties as well as performance `[shih2012]`; performance matters at lower levels `[landry2017]` and interacts with patronage `[jiang2018]`. Leaders time policy around promotion calendars `[chenzhang2021]`. China shows authoritarian responsiveness `[chenpanxu2016]`, constituency service `[distelhorst2017]` and conditional receptivity to participation `[meng2017]`. Informal institutions provide accountability `[tsai2007]`. Co-optation works through the NPC `[truex2014]`, `[truex2016]`. Public opinion has a coherent ideological structure `[panxu2018]`.

**Contested.** Whether local innovation survives vested interests `[lorentzen2014jop]`. Whether Xi-era centralization ended the decentralized model, and how state-business relations shifted toward mutual endangerment `[rithmire2023]`. Historical state building rested on elite kin networks `[wang2022]`.

**Gaps.** Most of this research uses data from before 2015. Recentralization, anti-corruption purges, the security turn in governance (`[greitens2020]`; see Pearson, Rithmire & Tsai in the IPE map) and reduced data access mean the field's core findings need re-testing under Xi.

## 6. State capacity, state building and historical legacies

**Claimed.** War made states `[tilly1990]`. Where war was absent and borders fixed, states stayed weak `[herbst2000]`. Contentious politics drives state building and durable autocracy `[slater2010]`. Colonial institutions shape development `[ajr2001]`.

**Settled.** Historical legacies persist: colonial forced labor `[dell2010]`, slavery `[acharya2016]`, political violence `[lupupeisakhin2017]` and precolonial conflict `[besley2014]` all leave measurable traces. Feudal constraints help explain Western divergence `[blaydeschaney2013]`, `[blaydes2018]`. Infrastructural power can be measured `[soifer2008]`. Weak formal institutions need their own theories `[levitskymurillo2009]`.

**Contested.** Kinship networks can support rather than undermine state building `[wang2022]`. Strong property rights can block infrastructure `[holland2023]`. Missionaries rival settler institutions as an explanation of democracy `[woodberry2012]`.

**Gap.** The persistence literature identifies effects better than mechanisms. Text-based measures of beliefs and institutions over long periods could trace how legacies are transmitted.

## 7. Political economy of development

Institutions cause development `[northweingast1989]`, `[ajr2001]`, but elites block growth-enhancing institutions when they fear replacement `[acemoglurobinson2006apsr]`. Redistribution takes inefficient forms to preserve power `[acemoglurobinson2001]`. Partial-reform winners capture states `[hellman1998]`. Democracy has no direct effect on growth but helps indirectly `[doucouliagos2008]`, and deliberation matters more than regime type for stability `[chandrarudra2015]`. Democracy does not make the poor better off `[ross2006]`. Governance indicators are contaminated by growth `[kurtzschrank2007]`. Democracies select more educated leaders `[besley2011]` but face more banking crises `[lipscy2018]`.

**Gap.** China and Vietnam complicate the institutions-first story (state-led growth without secure property rights). This has been studied mostly with single-country designs. A comparative framework covering developmental autocracies (Vietnam, Rwanda, Ethiopia, the Gulf) is still missing.

## 8. Resource curse and rentier states

Oil impedes democracy `[ross2001]`, but not within countries over time `[habermenaldo2011]`. The review consensus is that oil prolongs authoritarian rule in some settings while effects on growth are contested `[ross2015]`. Oil lowers women's status `[ross2008]` and lets dictators suppress media `[egorov2009]`. Nontax revenue stabilizes all regimes `[morrison2009]`.

**Gap.** The energy transition will devalue fossil rents. How petrostates adapt politically (diversification, repression, external investment) is a forward-looking question that connects to the IPE map's climate asset-revaluation work.

## 9. Redistribution, inequality and welfare states

**Claimed.** Redistribution rises as the median voter gets poorer relative to the mean `[meltzerrichard1981]`. Welfare regimes reflect class power `[espingandersen1990]`, `[cameron1978]`.

**Settled.** The median-voter prediction fails in its simple form. Insurance motives `[moenewallerstein2003]`, `[rehm2011]`, `[rehm2009]`, the skew of inequality `[lupupontusson2011]` and national identity `[shayo2009]` all change it. Electoral institutions shape redistribution through coalitions `[iversensoskice2006]`. Preferences have two facets `[cavailletrump2015]` and respond to job loss `[margalit2013]` and housing wealth `[ansell2014]`. Mass warfare, not democratization, produced progressive taxation `[schevestasavage2012]`, `[schevestasavage2010]`.

**Contested.** Social democrats favor insiders `[rueda2006]`. In developing countries, informality and fiscal capacity change everything `[mares2009]`, and left parties tolerate informality `[feierherd2022]`. Globalization constrains or enables welfare states `[garrett1998]`, `[rudra2002]`.

**Gap.** Redistribution politics in middle-income autocracies (China, Vietnam, the Gulf) is barely studied with the tools built for OECD democracies.

## 10. Varieties of capitalism and comparative political economy

Liberal and coordinated market economies rest on complementary institutions `[hallsoskice2001]`, which raise growth `[hallgingerich2009]`. The power-resources critique says welfare states reflect labor's strength, not employers' preferences `[korpi2006]`. Skill regimes differ by partisan path `[iversenstephens2008]`. Eastern Europe forms a dependent-market variety `[nolke2009]`. Liberalization trajectories differ within varieties `[thelen2012]`. Occupations shape preferences `[kitscheltrehm2014]`, conditioned by institutions `[gingrichansell2012]`, and party competition over welfare now involves new coalitions `[hausermann2013]`, `[oeschrennwald2018]`.

**Gap.** Varieties-of-capitalism theory has struggled to fit China and other state capitalisms. A typology that includes party-state capitalism (see the IPE map) would connect comparative political economy to geoeconomics.

## 11. Parties, party systems and electoral institutions

Consensus democracies perform well `[lijphart1999]`. Electoral rules limit parties through strategic coordination `[cox1997]`. Veto players explain policy stability `[tsebelis1995]`. Congruence is similar across PR and majoritarian systems `[golderstramski2009]`, and low-magnitude PR offers a sweet spot `[careyhix2011]`. Polarization matters more than fragmentation `[dalton2008]`. Party membership is declining `[vanbiezen2012]`, post-communist volatility comes from party entry and exit `[powelltucker2013]`, and niche parties are penalized for moderating `[adams2006]`. Parties set agendas `[eriksen2026]` but also follow supporters `[barbera2019]`.

**Gap.** Text-as-data methods (e.g. `[eriksen2026]`) now let researchers measure party strategy at scale across countries. Comparative party research outside Europe and the Americas has not yet caught up.

## 12. Populism and the radical right

**Claimed.** Populism is a thin ideology pitting the pure people against the corrupt elite `[mudde2004]`. Globalization created an integration-demarcation cleavage `[kriesi2006]` that politicized European integration `[hooghemarks2009]`.

**Settled.** Populism can be measured in voters `[akkerman2014]`, `[vanhauwaert2018]`, party communication `[jagers2007]` and speeches `[hawkins2009]`, and the ideational approach is now standard `[mudde2018]`. Immigration grievances unite radical right voters `[ivarsflaten2008]`, `[rydgren2008]`. Radical right success shifts mainstream positions `[abouchadikrause2020]`, though policy effects are limited `[mudde2013]`. Class voting is now tripolar `[oeschrennwald2018]`.

**Contested.** Cultural backlash `[norris2019]`, `[mutz2018]` versus economic roots `[colantone2018]`, `[broz2021]`, `[ballardrosa2021]`, with modest economic effects `[margalit2019]`, as reviewed in `[walter2021]` and `[golder2016]`. Financial crises feed extremes `[funke2016]`. Populism and technocracy are twin challenges to party government `[caramani2017]`. Left populism in Latin America produced authoritarian drift `[weyland2013]`.

**Gaps.** The IPE map's Section 3 covers economic backlash in depth. The comparative gap is populism in power: what populist governments do to institutions, bureaucracies and courts across regions (India, Turkey, Hungary, Mexico, Brazil, the US) in a common framework.

## 13. Clientelism, distributive politics and accountability

Machines monitor voters `[stokes2005]` and buy turnout `[nichter2008]` through brokers whose effort parties must monitor `[larreguy2016]`. Clientelism mixes inducements and coercion `[mares2016]` and is defined by contingency and iteration `[hicken2011]`. Young democracies rely on it because programmatic promises are not credible `[keefer2007]`. Clientelist appeals work `[wantchekon2003]`. Linkages vary systematically `[kitschelt2007]`, and distributive targeting depends on information `[goldenmin2013]`. Accountability conflates selection and sanctioning `[ashworth2012]`, and voters punish corruption only with credible information `[weitzshapiro2017]`.

**Gap.** Digital payments and biometric ID are changing how benefits are delivered (India's direct transfers, Brazil's Pix). Whether they weaken brokers, as the theory predicts, is a natural experiment in progress.

## 14. Ethnic politics and identity

Ethnic identity is descent-based and constructed `[chandra2006]`. Its salience depends on group size relative to the arena `[posner2004]` and rises near competitive elections `[eifert2010]`. Diversity undermines public goods through sanctioning, not preferences `[habyarimana2007]`. Leaders favor coethnics `[franck2012]`. Cross-cutting ties reduce ethnic voting `[dunningharrison2010]`, and party ties override caste quotas `[dunningnilekani2013]`. Modernization strengthens national identity `[robinson2014]`. Civic networks restrain riots `[varshney2001]`. Interethnic peace is the norm `[fearonlaitin1996]`; ethnic exclusion, not diversity, predicts conflict `[cedermangirardin2007]`, `[cederman2010]`.

**Gap.** The field moved from cross-national correlations to micro-experiments in a few countries (Uganda, Mali, India, Kenya). Integrating micro findings across cases remains hard.

## 15. Protest, civil society and contentious politics

Opportunity structures shape movement strategies `[kitschelt1986]`, but preference falsification makes revolutions unpredictable `[kuran1991]`. Nonviolent campaigns succeed more often `[stephanchenoweth2008]`, and revolutionary coalitions are thin `[beissinger2013]`. Civil society can sustain democracy `[putnam1993]` or undermine it `[berman1997]`. Institutions create trust, not the reverse `[rothsteinstolle2008]`. Repression's effects are non-monotonic `[zhukov2023]` and depend on credibility `[rozenaszhukov2019]`, as reviewed in `[davenport2007arps]` and `[hilljones2014]`. Protest helps elite coordination in coups `[caspertyson2014]`.

**Gap.** Nonviolent campaign success rates have fallen since 2010. Why (regime learning, digital surveillance, fragmented movements) is an open and important question.

## 16. Corruption, bureaucracy and courts

Corruption perceptions track development and democracy, but experience-based measures differ `[treisman2007]`. Corruption and distrust reinforce each other `[morris2010]`. Judicial independence varies across regimes `[helmke2009]`, and judges respond to career incentives `[perezlinan2006]`. Personnel control shapes bureaucratic incentives in China `[lizhou2005]`, `[jiang2018]`.

**Gap.** Large-scale anti-corruption campaigns (China, Brazil, Indonesia) are rarely compared.

## 17. Gender and representation

Descriptive representation matters in specific contexts `[mansbridge1999]`. Quotas drive women's representation `[tripp2008]`, `[paxton2010]` and spending priorities `[claytonzetterberg2018]`, with representation translating into substance under some conditions `[wangnerud2009]`. Feminist movements drive policy `[htunweldon2012]`. Quotas interact with minority status `[hughes2011]`. Women's cabinet appointments follow institutions `[krookobrien2012]`. Violence against women in politics is a threat to democracy `[krook2017]`. Women are less heard in deliberation `[parthasarathy2019]`.

**Gap.** Autocracies adopt gender quotas for reputation (see the IR map). How quotas function inside autocratic legislatures is understudied.

## 18. Institutional theory and comparative method

Historical institutionalism explains origins and change `[thelen1999]` through path dependence `[pierson2000]`, critical junctures `[capoccia2007]`, `[soifer2012]` and gradual change `[mahoneythelen2010]`. Institutions can also change endogenously `[greiflaitin2004]`, and ideas matter `[schmidt2008]`. Method debates cover context and mechanisms `[falleti2009]`, qualitative inference `[mahoney2010]`, controlled comparison `[slaterziblatt2013]` and synthetic control `[abadie2015]`.

---

## Cross-cutting roadmap: where your work fits

1. **The new autocracies.** Sections 3, 4, 5 and 7 all rest on data from an era when autocracies were poorer and less connected. Re-testing authoritarian-institutions theories on wealthy, digitally capable, internationally integrated autocracies connects directly to your work on autocratic rise.
2. **International sources of domestic regime change.** Backsliding and authoritarian durability (Sections 2 and 3) are studied mostly as domestic processes. Your globalization and order-contestation work can bring external trade, finance and autocratic support into these models, which is the second image reversed applied to the 2020s.
3. **Measurement with text.** Aggrandizement, propaganda, populist rhetoric and party strategy (Sections 2, 4, 11 and 12) are all measured more and more from text. Validated LLM annotation is the enabling method and the bridge to your methods work.
4. **China under Xi.** Section 5's findings need re-testing after 2015, with the security turn in governance as a likely explanation of what changed.

## What I could not verify (flagged)

- **Anchors:** all new anchors were found in Crossref, many through reviews, reprint chapters or edited-volume records without author metadata. Thelen 1999 was confirmed directly as the *Annual Review* article.
- **Claims:** one-line claims and edge justifications for non-library works are my summaries, not checked against full text.
- **Coverage:** citation counts favor older and American work. I filtered out American politics and methods, but some comparative subfields are thin, including Latin American and African politics beyond clientelism and ethnicity, and South and Southeast Asia beyond India and Indonesia. Most 2023–2026 work is under-sampled.
- **Journals:** the *Journal of Democracy* list was fetched by its electronic ISSN after the print ISSN failed. *Democratization* and *Government and Opposition* were not pulled systematically.
