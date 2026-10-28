# The IPE literature, c. 2006–2026: where it went, what settled, what is open

A narrative companion to `graph.json` / `network.html` in this folder. The graph has 263 work nodes (98 from this repo's `papers.json`, 165 supplementary works), 19 theme nodes and 367 typed relations. 70 of the works were added after a citation-based coverage audit (see the end of this file); each section marks them under **Added after the coverage audit**. Each theme section below follows the same order: **what was claimed → what the evidence settled → what is contested → gaps and research opportunities**. Node ids in brackets (e.g. `[farrell2019]`) point to entries in `graph.json`.

**Provenance and caveats.** Claims for the 91 repo works are condensed from the "Theory & evidence" analyses already in `papers.json` (written from full text, with a few abstract-only exceptions noted in the node's `verified` field). Supplementary works are canonical pieces I added from my own knowledge of the field, not from a systematic search. On 2026-10-28 each was looked up in Crossref by title and first author: 101 of 102 were confirmed to exist, and the result is recorded in each node's `verified` field. The one I could not confirm is Colgan & Keohane 2017 (*Foreign Affairs* is not indexed in Crossref). A few venue or year details remain soft and are listed at the end. Johns & Pelc is 2014, not 2016 as often miscited. Three repo entries lack a firm year (Han et al. working paper; Baccini & Sattler; the IO 75th-anniversary pieces, which I dated 2021). The graph is deliberately larger than the 80–150 nodes requested because the seed corpus alone yields ~90 relevant works; use the theme and decade filters, or the "repo works only" toggle, to thin it.

A note on what "top IPE" means here. The brief named APSR, AJPS, JOP, IO, World Politics, IS, ISQ and BJPS. Several debates that matter most to your agenda (weaponized interdependence, geoeconomics, Chinese statecraft, the OEP critique) have their best recent work in *RIPE*, *International Security*, *Annual Reviews*, economics journals and books, so those are included where they anchor a debate.

---

## 1. Trade preferences: factors, sectors, skills, and the non-material turn

**Claimed.** The field began with a clean deductive chain: Stolper-Samuelson plus a political model predicts that trade shocks split societies along factor lines, with the configuration set by endowments `[rogowski1987]`; factor mobility decides whether the cleavage is class (Heckscher-Ohlin) or industry (Ricardo-Viner) `[hiscox2001]`. Taken to survey data, skill predicted trade preferences in the US `[scheve2001]` and, cross-nationally, the sign of the skill effect flipped with endowments as the theory requires `[mayda2005]`.

**Settled.** The skill gradient is real but is not mainly a labor-market effect. The education effect survives among the retired and tracks exposure to economic ideas `[hainmueller2006]`; sociotropic perceptions and out-group anxiety dominate self-interest, and the education coefficient largely proxies for ethnocentrism `[mansfield2009]`; most respondents cannot locate their own interest, and information treatments only partly re-align preferences `[rho2017]`. The repo's own analysis of Mansfield & Mutz flags this as the hinge of the debate. The same conclusion holds for immigration `[hainmueller2010]`, `[hainmueller2014]` and, with reciprocity and security framing, for FDI `[chilton2020]` against the skill-based account `[pandya2010]`.

**Contested.** Material accounts were revived at a finer grain. Occupational task content (routineness, offshorability) predicts protectionism net of sociotropic controls `[owen2017]`, and exposure interacted with occupational immobility predicts anti-globalization sentiment in the US `[bisbee2025]`. Elite cues and fairness beliefs add a third family: "trade is unfair" rhetoric moves meritocratic but anxious Americans `[ballardrosa2024]`; affect toward partner countries sorts preferences by geopolitical alignment `[carnegie2022]`. Historically, Scheve & Serlin's "spatial Rogowski" shows trade's economic winners can lose political power through migration `[scheve2024]`, and Flaherty & Rogowski argue superstar trade theories imply far more losers than the classical models counted `[flaherty2021]`.

**Added after the coverage audit.** Framing moves trade support sharply `[hiscox2006]`, and voters rarely know how their representatives vote on trade `[guisinger2009]`. Interests work through household and community context `[fordham2012]`. Relative gains and fairness drive evaluations of deals `[mutzkim2017]`, `[brutger2021]`. Material interests matter for trade and immigration but ideology for aid `[milnertingley2011]`. Perceived exposure and cultural concern together explain discontent `[margalit2012]`. Together these reinforce the non-material turn, with Fordham & Kleinberg as the main interest-based reply.

**Gaps and open questions.**
- *Reconciling the three families.* No paper yet estimates, in one design, the relative weight of task-based material exposure, sociotropic/identity concerns and elite cues on the same respondents over time. A panel with occupation-level exposure, partisan cue exposure and identity measures would arbitrate; the repo's Ballard-Rosa et al. panel is the closest template.
- *Geopolitical trade preferences outside the US and India.* `[carnegie2022]` is the only mass-level test of security externalities. Conjoints in third countries caught between the US and China (Vietnam, Korea, Germany, Brazil) could test whether ally/adversary framing travels, and whether it interacts with GVC position.
- *Preferences over new instruments.* Almost nothing exists on mass preferences over export controls, investment screening, subsidies or friend-shoring, as opposed to tariffs. Magistro et al.'s AI/offshoring conjoint (in `papers.json`) shows the method; the instruments are the gap.
- *LLM-measured preferences.* Open-ended trade attitudes (as in `[carnegie2022]`) are rarely used because coding is costly; LLM annotation with validation (Egami et al., Benoit et al. in the repo) makes free-text measurement of *reasons* for trade attitudes feasible at scale. This connects directly to your annotation work.

## 2. Embedded liberalism and compensation

**Claimed.** Postwar openness rested on a compromise: multilateral liberalization made compatible with domestic intervention for stability `[ruggie1982]`. Open economies therefore have bigger governments `[cameron1978]`, because spending insures against external risk `[rodrik1998]`, and globalization need not force policy convergence where encompassing labor and left parties persist `[garrett1998]`.

**Settled.** The macro correlation is robust but political rather than automatic: it holds in democracies and vanishes under authoritarianism `[adsera2002]`, and it reverses in developing countries where surplus labor cannot defend welfare `[rudra2002]`. The micro chain has been tested: social spending raises exposed workers' support for trade `[hays2005]`, exposure → insecurity → welfare demand → trade support holds at the individual level `[walter2010]`, and Trade Adjustment Assistance measurably blunts electoral punishment for trade layoffs `[margalit2011]` while substituting for protectionist demands `[kim2021taa]`. Whether a government can *commit* to compensation depends on constitutional structure and the geography of losers `[kim2025agri]`.

**Contested.** Whether the compromise still exists. The China-shock literature reads backlash as the breakdown of a non-credible compensation promise `[colantone2018]`, Colgan & Keohane blame elite capture `[colgan2017]`, and Zohlnhöfer et al. show the quantitative literature on the retreat of the interventionist state does not even agree on causes `[zohlnhofer2018]`. Goodman & Pepinsky argue the compromise was exclusionary from the start: it worked by denying migrants rights, and inclusion eroded it from below `[goodman2021]`. Baccini & Sattler add that backlash is partly policy-made (austerity × vulnerability) rather than only shock-driven `[baccini2024]`.

**Gaps and open questions.**
- *Compensation design, not amount.* We know compensation works at the margin and that it is politically unstable. We lack comparative evidence on *which* designs (place-based vs individual, retraining vs income support, pre-committed vs discretionary) are both effective and durable. The 2022-25 wave of industrial-policy spending (CHIPS, IRA, EU Green Deal Industrial Plan) is a natural experiment in place-based compensation that no top-journal paper has yet exploited electorally.
- *Compensation under geoeconomic shocks.* Who compensates losers from sanctions, export controls and decoupling (Chinese retaliation on US agriculture, European energy shock)? `[kim2021tariffs]` and `[blanchard2024]` show electoral effects; the compensation politics (farm bailouts, energy subsidies) is unstudied as a compensation case.
- *Developing-country compensation.* Rudra's line (`[rudra2002]`, `[rudra2005]`) has few recent followers using the firm-level or product-level data now available for Vietnam, Mexico, India. Your Globalization Grievance Index could be the dependent variable for a modern Rudra test.
- *Promissory costs of interdependence.* `[schneider2024]` opens a representational channel (pledge fulfillment) that could be extended to trade and industrial-policy pledges specifically.

## 3. Globalization backlash, the China shock, and populism

**Claimed.** Chinese import competition caused large, persistent local labor-market losses `[autor2013]` and then political polarization and the 2016 vote `[autor2020]`; the pattern recurs in Western Europe `[colantone2018]` and Brexit `[colantone2018brexit]`. Trade's winners also vote `[jensen2017]`. Economic shocks reach politics through authoritarian values `[ballardrosa2021]`, place-based decline `[broz2021]`, inequality from superstar dynamics `[flaherty2021]`, and long historical memory `[han2024]`. Financial crises, specifically, raise far-right vote shares `[funke2016]` and now punish incumbents regardless of bailouts `[chwieroth2019]`.

**Settled.** The *existence* of a causal path from trade shocks to right-populist voting in rich democracies is the best-replicated finding in modern IPE. The shift-share design, the European replications and the trade-war studies agree in sign. The targeted-tariff studies also settle that trade policy can be used as an electoral weapon by a foreign state `[kim2021tariffs]`, `[blanchard2024]`.

**Contested.** Three things. (i) *Magnitude*: Margalit shows trade shocks are "outcome significant" but explain a small share of variance `[margalit2019]`; cultural accounts `[norris2019]`, `[mutz2018]` claim the main effect. Rodrik's synthesis `[rodrik2018]`, `[rodrik2021]` and Walter's review `[walter2021]` argue for interaction, with economics underneath cultural expression. (ii) *Mechanism*: racialized group-status politics `[baccini2021]` vs. insecurity `[bisbee2025]` vs. place `[broz2021]` vs. elite cues `[ballardrosa2024]`. (iii) *Transmission*: De Vries, Hobolt & Walter argue grievance becomes institutional change only when challenger parties politicize it through permissive opportunity structures `[devries2021]`; Milner's three-pathway synthesis `[milner2021]` leaves open which pathway dominates where.

**Added after the coverage audit.** Legislators in China-shock districts vote more protectionist `[feigenbaum2015]`. A 2024 meta-analysis of causal studies finds globalization shocks raise populist support robustly but modestly, mostly on the right `[scheiring2024]`. That supports Margalit's "outcome significant but small" reading over both strong economic and purely cultural accounts. Adler-Nissen & Zarakol add a status-recognition account of order-level discontent `[adlernissen2021]`.

**Gaps and open questions.**
- *Backlash outside the OECD.* Nearly all evidence is US/European. A PEIO paper cited in the search found no right-wing shift from the China shock in emerging economies, and Milner's address calls for developing-country evidence. Your Globalization Grievance Index, if it covers the Global South, fills exactly this hole: do import shocks in middle-income democracies (Brazil, Indonesia, South Africa, Türkiye) produce left, right, or no backlash, and does the answer track compensation capacity (`[rudra2002]`)?
- *The second China shock and the export-controls shock.* Chinese EV, solar and battery exports after 2021 are a new shock to European and emerging-market manufacturing. No top-journal paper yet treats it with a shift-share design. Likewise the *supply-side* shock of US export controls on firms and regions in allied countries (Netherlands, Korea, Japan, Taiwan).
- *Backlash against geoeconomics.* Who loses from decoupling, and do they mobilize? Firm and worker exposure to sanctions/export-control compliance is measurable with customs and HS-6 dual-use data, which is where your dual-use classification can be a treatment variable.
- *Durability and reversal.* Does compensation or recovery reverse the political effect (Han et al. suggest persistence over a century)? Within-place panels over the 2016-2024 US cycle, where exposed counties received both tariffs and industrial-policy investment, could test reversibility.
- *Measurement of grievance.* The literature measures backlash by votes and single survey items. Text-based grievance measures (speeches, local news, social media) coded with validated LLM annotation would let researchers separate economic from cultural grievance in the same corpus and over time.

## 4. Firms, GVCs and the new trade politics

**Claimed.** Heterogeneous-firm trade theory `[melitz2003]` moved the unit of trade politics from factors and industries to firms. Productive exporters lobby individually for product-specific liberalization `[kim2017]`; in differentiated-goods industries, industry opposition dissolves because large exporters dominate position-taking `[osgood2017]`; the pro-trade coalition is defined by offshoring and imported inputs rather than export opportunities `[osgood2018]`; GVC linkages discipline tariffs `[blanchard2016]`; PTAs' gains concentrate in large multinational-linked firms `[baccini2017]`.

**Settled.** Within-industry variation in trade positions and lobbying is large and systematic, and GVC position predicts both preferences `[kim2019firms]` and policy outcomes. Kim & Osgood's review `[kim2019arps]` treats this as the field's consensus. Supply-chain ties also protect investors `[johns2016]` and coordinate lobbying `[zhang2023]`; FDI creates new pro-liberalization coalitions in host countries `[kim2025fdi]`.

**Contested.** How far the firm turn explains *backlash*: if large firms won the trade policy fight, the mass politics of Section 3 is a reaction to a firm-dominated regime (Flaherty & Rogowski's superstar argument makes this link). Whether supply chains diffuse standards upward is conditional `[malesky2018]`, while competitive races to the bottom appear not to exist once properly tested `[guasti2022]`.

**Added after the coverage audit.** Firm surveys confirm superstar exporters and importers are the most pro-trade firms `[osgood2017jop]`. Industries trading inside their own multinational supply chains file fewer trade-remedy petitions `[jensen2015]`. In solar, supply-chain position splits manufacturers from installers over tariffs `[meckling2017]`, an early clean-energy case of GVC trade politics.

**Gaps and open questions.**
- *Firms under geoeconomics.* The firm literature was built for liberalization. We have almost no systematic evidence on how firms position themselves on export controls, screening, sanctions compliance and friend-shoring, where the "productive exporter wants openness" logic may invert (national champions may want protection from Chinese competition but access to Chinese inputs). Lobbying-disclosure data with LLM-coded issue content would reveal this.
- *GVC position and security exposure.* Kim et al.'s multidimensional conjoint `[kim2019firms]` could be re-run with security dimensions (data localization, dual-use licensing, origin rules). Your HS-6 dual-use classification gives the product-level exposure measure that this literature lacks.
- *Chinese and emerging-market firms.* Firm-level trade politics is overwhelmingly about US firms. Pearson, Rithmire & Tsai `[pearson2022]` and Rithmire `[rithmire2023]` describe party-state capitalism qualitatively; there is no quantitative firm-level study of Chinese firms' trade-policy positions or of how party cells alter them.
- *Firms and compensation.* Do firms that gain from liberalization support compensating losers (as the Ruggie bargain implies) or oppose it? This connects Sections 2 and 4 and is untested.

## 5. FDI, MNCs and investment regimes

**Claimed.** Democracies attract FDI through credibility `[jensen2003]`; trade agreements and their design features substitute for or reinforce that credibility `[buthe2008]`, `[buthe2014]`; FDI liberalization followed democratization and skilled-labor demand `[pandya2014]`.

**Settled.** Credible commitment devices work, and their *design* matters more than their count. But the regime-type story is heavily qualified: investor nationality communities shield firms more than regime type `[wellhausen2015]`, supply-chain ties shield further `[johns2016]`, BITs help autocracies most and prolong autocrats' tenure `[arias2018]`, and FDI stabilizes authoritarian rule `[bak2016]`.

**Contested.** Whether investment regimes are now reversing. The spread of investment screening across the EU `[bauerle2023]`, driven by Chinese investment and the securitization of economic policy `[meunier2019]`, `[pearson2022]`, means the dependent variable of twenty years of work (how to attract FDI) has flipped for a class of investors (how to exclude it).

**Added after the coverage audit.** The investment-treaty literature now sits in the graph. BITs spread as a competitive race for capital `[elkins2006]` and attract FDI by commitment and signaling `[kerner2009]`. Their credibility depends on arbitration records `[allee2011]`. States signed them with bounded rationality until the first claim hit `[poulsen2013]`, then redesigned treaties `[thompson2019]`. Simmons recasts the regime as asymmetric bargains now under contestation `[simmons2014]`. Also added: executive constraints as the democratic FDI mechanism `[jensen2008]`, diaspora networks `[leblang2010]`, FDI empowering Vietnamese provinces `[malesky2008]`, the rise of transnational state capital `[babic2019]`, and member-state support for EU screening `[chan2021]`.

**Gaps and open questions.**
- *The political economy of investment screening.* Bauerle Danzman & Meunier map designs; no one has yet explained screening *decisions* (which deals are blocked, by whom, with what domestic coalitions) across countries with firm-level data, nor measured the chilling effect on FDI by origin and sector.
- *Autocratic outward investment as statecraft.* Dreher et al. `[dreher2022]` cover Chinese official finance; Chinese *private and SOE* outward FDI as a tool of influence (and the host backlash) lacks a Jensen-style cross-national study.
- *Host-country politics of Chinese FDI.* Does Chinese greenfield investment create pro-China coalitions the way `[kim2025fdi]` shows FDI creates pro-trade coalitions? This is a direct extension with available fDi Markets data.
- *Investor-state dispute settlement legitimacy.* The ISDS backlash (withdrawals, carve-outs) is barely studied with the tools used for WTO litigation `[davis2012]`, `[pelc2014]`.

## 6. Exchange rates, sovereign debt and financial crises

**Claimed.** Capital mobility shifts conflict to sectors defined by asset specificity and tradability, predicting currency preferences `[frieden1991]`; monetary institutions are domestic distributional choices `[bernhard2002]`; markets constrain governments narrowly in rich countries and broadly in poor ones `[mosley2003]`; sovereign lending runs on reputation `[tomz2007]`; democracies enjoy a financial advantage `[schultz2003]`.

**Settled.** The sectoral/asset approach to currency politics is the working consensus, and it extends to autocratic subtypes `[steinberg2014]`, state-controlled finance `[steinberg2015]` and default as a distributional choice `[ballardrosa2020]`. Financial crises have distinctive political effects (extremism, incumbent punishment) `[funke2016]`, `[chwieroth2019]`. The Eurozone crisis was a distributional fight over adjustment `[frieden2017]`, and exposed voters respond to targeted bailout promises `[ahlquist2020]`.

**Contested.** The democratic advantage: Lipscy shows the same institutional features that give democracies credit also make them crisis-prone `[lipscy2018]`. The IMF's role is contested between informal US control `[stone2008]`, common agency `[copelovitch2010]`, geopolitical vote-buying `[dreher2009]`, shared beliefs `[nelson2014]`, and asymmetric moral hazard with reserve hoarding `[lipscy2019]`. The dollar's future is contested between structural persistence `[strange1987]`, `[winecoff2020]`, privilege-taking that frays as security leverage declines `[mastanduno2009]`, instability generated by US buildups `[oatley2015]`, and sanctions-driven hedging `[mcdowell2023]`.

**Added after the coverage audit.** The democratic advantage in sovereign debt is qualified twice: it lies in market access more than price `[beaulieu2012]`, and it depends on global liquidity cycles `[ballardrosa2019]`. Central bank independence works best where democratic institutions make it credible `[bodea2015io]`. Neoliberal-trained economists sped capital-account liberalization `[chwieroth2007]`. Remittances make fixed exchange rates cheaper `[singer2010]`. The 2008 crisis is read as Knightian uncertainty rather than risk `[nelson2014ik]`. On China, Drezner shows creditor leverage is weaker than feared `[drezner2009]`.

**Gaps and open questions.**
- *Currency politics under weaponized finance.* Frieden's sectoral model predates sanctions on central banks. Which domestic groups in China, India, Gulf states and Brazil push for de-dollarization or CBDC settlement, and why? McDowell's country cases could be turned into a sectoral-preference study.
- *Sovereign debt with China as creditor.* Debt distress in 2020-25 involved Chinese lenders outside the Paris Club. Reputation `[tomz2007]` and distributional `[ballardrosa2020]` theories were built for Western creditors; whether borrowers treat Chinese and Western creditors differently, and how China's lending interacts with IMF programs `[clark2022imf]`, is open.
- *Macro-IPE after reductionism.* Blyth & Matthijs' "missing macroeconomy" `[blyth2017]` has not been answered with top-journal empirical work linking growth regimes to IPE outcomes; the inflation shock of 2021-23 and its distributional politics is an obvious case.
- *Exchange-rate politics of developing-country manufacturing exporters* (Steinberg's cases) under the second China shock: do undervaluation coalitions re-form or fracture when the competitor is China rather than the US?

## 7. IMF, World Bank and informal governance

**Claimed.** IOs run on formal rules plus informal great-power access `[stone2008]`; staff anticipate the principal `[clark2021wb]`, `[carnegie2023]`; influence is redistributed only where exit options are credible `[lipscy2015]`, `[lipscy2017]`.

**Settled.** Informal US (and G5) influence is well documented across lending size, conditions, waivers and reforms. The outside-options theory has survived two sharp tests: competing regional arrangements lower IMF conditionality `[clark2022imf]`, and AIIB founding cut World Bank infrastructure borrowing `[qian2023]`.

**Contested.** Whether Chinese finance is a rival *order* or a commercially driven outside option `[dreher2022]`, `[broz2020china]`; and whether IFIs now actively prop up autocracies: Cottiero & Schneider show autocracy-dominated IFIs lend to threatened autocrats `[cottiero2026]`, extending Debre's regional-organization finding `[debre2021]` and reversing the democracy-locking view of IO membership `[mansfield2006]`.

**Added after the coverage audit.** New conditionality data show IMF conditions did not fall after the 2000s reforms `[kentikelenis2016]`. IMF programs cut spending, but democracies protect social spending `[nooruddin2006]`. Strong labor wins softer labor conditions `[caraway2012]`. Staff exercise informal governance of their own `[chwieroth2013]`. Overlapping development IOs pool when their leading shareholders are aligned `[clark2021pool]`. Both the WTO and the IMF adapted imperfectly to rising powers `[zangl2016]`. Donor influence extends to the Asian Development Bank `[kilby2006]`.

**Gaps and open questions.**
- *Autocratic IFIs as a system.* `[cottiero2026]` is new. The next steps are conditionality content (what do autocratic lenders ask for?), interaction with IMF programs, and whether recipients' behavior (repression, election manipulation) changes after such loans. This is squarely in your "autocratic rise" agenda.
- *Informal governance in new institutions.* Stone's framework has not been applied to the AIIB, NDB or the BRI's financing bodies: is China's informal access structured like the US's at the IMF?
- *Staff anticipation measured with text.* Clark & Dolan infer anticipation from outcomes; loan documents, board minutes and staff reports are now machine-readable, so anticipation of principal preferences could be measured directly in text with validated LLM coding.

## 8. GATT/WTO, PTAs and institutional design

**Claimed.** Democracies trade more freely with each other `[mmr2000]` and sign more agreements to signal to voters `[mmr2002]`; flexibility (escape clauses) makes agreements self-enforcing `[rosendorff2001]`, `[kucik2008]`; issue linkage builds liberalizing coalitions `[davis2004]`; litigation is driven by domestic constituencies `[davis2012]` and by precedent-seeking `[pelc2014]`.

**Settled.** After Rose's null `[rose2004]`, the trade effects of the GATT/WTO were re-established once participation was coded properly `[goldstein2007]`, though concentrated among major powers `[gowa2005]` and politically dissimilar dyads facing hold-up `[carnegie2014]`. PTA design varies with domestic institutions and GVCs, and effects run through depth `[baccini2019]`, `[mansfield2012]`, `[buthe2014]`, `[kim2025agri]`. Democracy changes the *form* of protection toward opaque measures `[kono2006]`, including state media `[kim2018media]`.

**Contested.** Whether the rulebook still fits the instruments states use. Bown argues WTO rules built for tariffs cannot discipline modern industrial policy `[bown2024]`; the Appellate Body's collapse and the shift to subsidies, export controls and security exceptions mean the dependent variables of the design literature (tariff bindings, dispute filings) are losing relevance.

**Added after the coverage audit.** The DESTA dataset shows deep PTAs raise trade far more than shallow ones `[dur2014]`, and PTA texts are largely copied from templates `[allee2019]`. The dispute-settlement strand is now represented. States shop for forums `[busch2007]`, third parties hinder settlement `[busch2006]`, and legal experience decides who files `[davisbermeo2009]`. Institutions also reduce trade volatility `[mansfield2008]`. Accession is geopolitical `[daviswilf2017]`, and gains come from rigorous accession commitments `[allee2012]`. Brazil, India and China broke into the regime's core by different routes `[hopewell2014]`, and China contests the trade order selectively `[weinhardt2019]`.

**Gaps and open questions.**
- *Design of geoeconomic agreements.* The IPEF, EU trade-and-technology council, critical-minerals agreements and "friend-shoring" clubs are new institutional forms with no PTA-style design dataset. A DESTA-like coding of security provisions, origin rules and export-control coordination in post-2018 agreements would be a public good and a dissertation.
- *Security exceptions and WTO legitimacy.* GATT Article XXI litigation (Russia–Transit, US–Steel) tests whether the regime can adjudicate security claims; no political-science study yet models when states invoke security exceptions and how panels respond.
- *Regulatory and health-standard protectionism as retribution.* `[kim2025refusals]` shows border inspections double as punishment. Comparable data exist for the US, EU and India (import alerts, SPS notifications) and could test whether democracies also do this.
- *Who benefits from rules under decoupling?* Carnegie's hold-up logic `[carnegie2014]` predicts that rivals gain most from institutions; the US–China trade war offers a test of what happens to rival-dyad trade when the institution stops working.

## 9. Weaponized interdependence, sanctions and economic statecraft

**Claimed.** Asymmetric dependence yields influence `[hirschman1945]`; sanctions work mainly at the threat stage `[drezner2003]`; global networks form hubs whose controllers can surveil (panopticon) or cut off (chokepoint) `[farrell2019]`.

**Settled.** The network view displaced bilateral dependence as the default framework within five years, and its core descriptive claims (US control of financial messaging, dollar clearing, chip tooling) are not disputed `[drezner2021]`, `[farrell2023]`. Sanctions research settled earlier that threats matter more than imposition `[grauvogel2017]`, that firms, not black knights, drive busting `[early2009]`, and that informal, deniable coercion is China's modal form `[lim2022]`, `[kim2025refusals]`, `[fuchs2013]`.

**Contested.** The limits. Markets adjust around chokepoints `[gholz2021]`; private hub owners resist states `[gjesvik2023]`; targets hedge by de-dollarizing `[mcdowell2023]`; interwar history shows sanctions drove revisionists toward autarky and war `[mulder2022]`; state control over commercial actors is a precondition China often lacks `[norris2016]`; and trade dependence rarely buys policy deference `[kastner2016]` against `[floresmacias2013]`. Whether the economic realm is now a security dilemma `[pearson2022]` or still "business as usual" `[davis2011]` is the live question.

**Added after the coverage audit.** Sanctions increase repression in targets `[wood2008]` and succeed more often when major trading partners impose them `[mclean2010]`. They also serve presidents' domestic audiences `[whang2011]`. They cost the sender's own investors `[biglaiser2011]`, who reroute FDI through third parties `[barry2015]`. Chen & Evers theorize supply-chain chokepoints as a power-transition strategy `[chenevers2023]`.

**Gaps and open questions.**
- *Effectiveness with a comparable dataset.* There is no TIES-style dataset of export controls, entity listings, investment bans and informal Chinese measures after 2018 coded with outcomes. Building one (with HS-6 dual-use coverage) would let the field replicate the sanctions-effectiveness debate for the new instruments.
- *Domestic politics of weaponization in the hub state.* Farrell & Newman specify "suitable domestic institutions" but do not model the coalition politics of using chokepoints (firms that lose sales vs. security agencies). Lobbying and comment data on BIS rules are available.
- *Third-country responses.* Who complies, who busts, who hedges? Early's firm-driven busting logic `[early2009]` has not been tested on Russia 2022 or on China export controls; trade-diversion data make this feasible now.
- *Measurement of network position.* Winecoff's and Farrell-Newman's hub claims rest on aggregate flows. Product-level, firm-level network measures of chokepoint exposure (where your dual-use classification is the natural filter) do not yet exist in political science.
- *The weaponization–legitimacy link.* Do publics in targeted or third countries turn against the hub state (McDowell's hedging at the mass level)? Mattingly et al.'s 19-country experiment design (in `papers.json`) could test it.

## 10. Industrial policy, economic security and geoeconomics

**Claimed.** Industrial policy is back and can work; its constraints are political economy and state capacity `[juhasz2024]`; neomercantilist thought has a long and global pedigree IPE wrote out `[helleiner2021]`; the EU geopoliticized trade and investment policy `[meunier2019]`; the CCP securitized economic governance into party-state capitalism, triggering an economic security dilemma `[pearson2022]`, `[rithmire2023]`; energy mercantilism is rational supply-chain management `[lind2018]`.

**Settled.** Very little, empirically. The descriptive turn is agreed (states are using subsidies, screening, controls at scale: Bown documents the drivers `[bown2024]`), and the economics now accepts conditional effectiveness. Mastanduno's prediction that unipolarity and perceived decline reintegrate economics and security `[mastanduno1998]` reads as prescient.

**Contested.** Almost everything causal: whether security motives or protectionist rent-seeking drive policy; whether party-state capitalism is a response to threat or a project of control; whether decoupling is happening or re-routing; whether climate asset revaluation `[colgan2021]` or great-power rivalry is the stronger driver of trade restriction. The web search for 2024-26 canonical pieces returned mostly working papers, special-issue introductions and think-tank work; this is a debate without an empirical anchor yet (flag: I could not verify a top-journal empirical article on economic-security policy choice).

**Added after the coverage audit.** Made in China 2025 is analyzed as a challenge to US structural power over intellectual property and production `[malkin2020]`. State-led foreign investment is a structural shift behind economic-security politics `[babic2019]`. Helleiner frames the moment as a polycrisis of interacting shocks `[helleiner2024]`.

**Gaps and open questions.**
- *A theory of industrial-policy coalitions.* OEP's toolkit (interests from factor/sector/firm position, institutions, bargaining) has not been applied systematically to who demands and who gets industrial-policy money across the US, EU, Japan, Korea and China. Lobbying, subsidy and procurement microdata exist.
- *Security vs. protection: a measurement problem.* Separating security-motivated from protectionist measures is the field's central identification problem. Product-level dual-use intensity (your HS-6 classification) gives a direct test: measures concentrated on dual-use lines look like security policy; measures on non-dual-use lines in politically sensitive districts look like protection.
- *Allied coordination and free-riding.* Export-control alignment (Netherlands, Japan with the US) is a classic collective-action problem with alliance variables; no one has modeled it with the tools used for multilateral sanctions coalitions (Bapat & Morgan 2009, not in graph).
- *Party-state capitalism measured.* Pearson, Rithmire & Tsai is qualitative. Party-cell presence, state fund stakes and political red-line enforcement across listed Chinese firms are codable from filings and could be linked to firms' export, investment and lobbying behavior abroad, and to foreign screening decisions.
- *Developing countries in a geoeconomic order.* The special issue the search surfaced ("industrial policy beyond the hegemons") is a sign the gap is recognized; the IPE of middle powers' hedging between the US and China (Vietnam, India, Indonesia, Gulf) is wide open and connects to Sections 7 and 11.

## 11. China's rise and contestation of the liberal order

**Claimed.** The order's crisis is one of authority within the West `[ikenberry2018]`, or of elite capture `[colgan2017]`, or structurally fated by the end of unipolarity `[mearsheimer2019]`, or endogenous to intrusive postnational liberalism `[borzel2021]`, or built on de-bordering that erodes territorial foundations `[simmons2021]`, or self-undermining in the information domain `[farrell2021]`. China's strategy follows network position `[goddard2018]`, issue-specific orders `[johnston2019]`, regime pillars and domestic heterogeneity `[weiss2021]`; followers are pushed by grievances with the US-led financial order `[broz2020china]`.

**Settled.** That the LIO is internally contested and that China is selectively, not uniformly, revisionist (`[johnston2019]`, `[weiss2021]`, and Lake, Martin & Risse's stocktaking `[lake2021]`). Chinese finance creates real outside options `[qian2023]`, `[dreher2022]`. Authoritarian regional organizations and IFIs protect incumbents `[debre2021]`, `[cottiero2026]`, `[ginsburg2020]`.

**Contested.** Whether domestic backlash (Section 3) and external challenge interact or are separable; whether China exports a model (Mattingly et al. in the repo show state media persuades global audiences) or merely offers finance; and whether "order" is the right unit at all versus issue-specific regimes.

**Added after the coverage audit.** Chinese state media persuades global audiences of the China model `[mattingly2025]`. The new aid theme (Section 19) adds evidence that Chinese aid follows political alignment `[dreher2018]` but buys limited soft power `[blair2021]`.

**Gaps and open questions.**
- *Measuring order contestation.* Beyond UN votes and IO membership, there is no standard measure of states' positions toward competing orders across issue areas. Text of leaders' speeches, IO statements and treaty language could be coded for alignment with liberal vs. sovereigntist framings, which is a task well suited to validated LLM annotation and directly to your order-contestation work.
- *Middle-power hedging as a dependent variable.* Broz, Zhang & Wang use one event (BRF attendance). A panel of hedging behavior (AIIB membership, Huawei decisions, BRI participation, export-control alignment, UN votes) would let one test push vs. pull systematically.
- *The authoritarian economic order.* Debre, Ginsburg and Cottiero & Schneider describe the pieces; nobody has assembled them into a test of whether an autocratic economic governance complex (SCO, BRICS bank, CIPS, autocratic IFIs) functions as an order with its own compensation and commitment devices, or is a loose hedge.
- *Interaction of backlash and rivalry.* Do domestic populists in democracies make states more or less able to compete with China (trade-war support vs. alliance erosion)? Carnegie & Gaikwad's geopolitical preferences and Kim & Margalit's tariff targeting point to a research design.

## 12. Regime type, autocracies and the global economy

**Claimed.** Democracies trade more with each other `[mmr2000]`, democratization drove developing-country liberalization `[milner2005]`, and IO membership locks in democratic reform `[mansfield2006]`, `[baccini2014]`.

**Settled.** Autocracies are heterogeneous in ways that matter as much as the democracy divide: institutionalized autocracies trade more openly `[hankla2013]`, subtypes choose different exchange-rate regimes `[steinberg2014]` and default differently `[ballardrosa2020]`; autocrats use BITs and FDI as substitutes for domestic credibility and as survival tools `[arias2018]`, `[bak2016]`; they manage information strategically `[hollyer2018]`; democracy changes the form, not just the level, of protection `[kono2006]`; democracies are more crisis-prone `[lipscy2018]`; and financial openness can push unequal autocracies toward democracy `[freeman2012]`, with social spending as the condition for openness to help democracy `[rudra2005]`.

**Contested.** Whether international economic institutions now on net support autocracy (Sections 7 and 11) rather than democratization, which would reverse the 2000s consensus.

**Gaps and open questions.**
- *Autocratic learning and the global economy.* How autocracies adapt economic policy to international pressure (sanctions, screening, IMF programs) with regime-survival rather than welfare objectives is theorized case by case (Russia, China, Iran) but not comparatively with the regime-subtype data used in `[hankla2013]` and `[steinberg2014]`.
- *Economic statecraft by non-Chinese autocracies.* Gulf sovereign funds, Russian energy coercion and Turkish trade diplomacy are rarely studied with the Norris/Lim-Ferguson toolkit.
- *Does openness still liberalize?* The 1990s-2000s evidence that trade and finance open autocracies politically (`[rudra2005]`, `[freeman2012]`) has not been re-estimated for the 2010s, when the rising autocracies were also the most integrated.

## 13. Migration politics

**Claimed.** Skilled natives favor immigration where immigrants are unskilled `[mayda2006]`; trade and capital openness close low-skill borders by removing firms' lobbying `[peters2014]`, `[peters2017]`; responsive institutions restrict labor openness `[bearce2017]`.

**Settled.** Individual self-interest explains little of immigration attitudes; sociotropic and cultural concerns dominate `[hainmueller2010]`, `[hainmueller2014]`. The trade-immigration substitution at the policy level is well supported. Firms still win firm-specific relief for high-skill visas through bureaucratic lobbying `[liao2023]`. Migration can itself foster cosmopolitanism among migrants `[gaikwad2025]`. The postwar compromise depended on migrants' exclusion `[goodman2021]`.

**Contested.** How migration backlash relates to trade backlash: Rodrik treats immigration salience as what makes populism right-wing `[rodrik2018]`; Simmons & Goemans see re-bordering as a structural reaction to the LIO `[simmons2021]`.

**Added after the coverage audit.** Labor-market threat drives opposition to high-skilled immigration among directly competing workers `[malhotra2013]`. Sectoral growth or decline shapes immigration attitudes `[dancygier2013]`. Border walls cut trade between neighbors `[carter2019]`.

**Gaps and open questions.**
- *Migration as a geoeconomic instrument.* Talent controls (student-visa restrictions on Chinese STEM students, researcher screening) are economic-security policy with no IPE literature; Liao's visa data approach could be extended.
- *Remittance and diaspora politics under sanctions* (Russia, Venezuela, Iran) sits between migration and statecraft and is unstudied in top journals.

## 14. IPE's self-critique: OEP, the new interdependence approach, structural power

**Claimed.** OEP organized the field as interests → institutions → bargaining `[lake2009]`, descended from the second image reversed `[gourevitch1978]`. Critics charged reductionism that omits systemic feedback `[oatley2011]`, loss of geopolitics `[drezner2013mcnamara]`, loss of the macroeconomy `[blyth2017]`, and neglect of cross-jurisdictional opportunity structures `[farrell2014]`, `[farrell2016]`. Structural power persists as network centrality `[strange1987]`, `[winecoff2020]`.

**Settled.** The critique was absorbed rather than refuted: Chaudoin, Milner & Pang showed systemic interactions can be modeled within OEP `[chaudoin2015]`; the weaponized-interdependence program `[farrell2019]` is the new interdependence approach's success; the 75th-anniversary IO issue `[lake2021]` conceded the "blind spots" (exclusion, interests behind rules, social foundations, domestic politics of order).

**Contested.** Whether the field now has a theory of *systemic change* (Drezner & McNamara's demand) or only better-specified domestic models. Helleiner's recovery of neomercantilism `[helleiner2021]` and Colgan, Green & Hale's dynamic asset-revaluation politics `[colgan2021]` are candidate frameworks.

**Gaps and open questions.**
- *An OEP of economic security.* The cleanest contribution available to a dissertation is to do for geoeconomics what Rogowski/Frieden did for trade and finance: derive actors' interests over export controls, screening and subsidies from their position (dual-use exposure, GVC node, asset specificity), then test with lobbying and voting data. Sections 4, 9 and 10 all point here.
- *Feedback from statecraft to domestic coalitions.* Weaponization changes who the winners and losers of openness are (sanctions compliance costs, re-shoring subsidies), which should feed back into the preferences studied in Sections 1-3. No paper closes that loop.
- *Methodological: text as the missing data layer.* Many of the gaps above are measurement gaps (grievance, order alignment, security vs. protection motives, staff anticipation, firm positions on controls). Validated LLM annotation with design-based correction (Egami et al. in the repo) is the enabling method, and IPE has barely used it.

## 15. Trade, interdependence and conflict

**Claimed and settled.** Alliances structure trade through security externalities `[gowa1993]`; development and openness rather than democracy underpin the liberal peace `[gartzke2007]`; bilateral trade pacifies while multilateral openness can raise conflict `[martin2008]`; expectations of future trade decide whether dependence pacifies or provokes `[copeland2015]`. Political tensions disrupt trade less than theory predicts `[davis2011]`.

**Contested.** Whether the economic realm has entered security-dilemma dynamics `[pearson2022]` that invalidate "business as usual," and whether mass publics now weigh security externalities in trade preferences `[carnegie2022]`.

**Gaps.** Trade-expectations theory predicts that negative expectations (decoupling talk, export controls) raise conflict risk; the 2018-2026 period is the first out-of-sample test, and firm-level expectation measures (earnings calls, supply-chain announcements) could operationalize Copeland's variable for the first time.

## 16. Diffusion, transgovernmental networks and regulation

Liberal policies diffused through competition and information `[simmons2004]`; bilateral regulator ties drive adoption while multilateral forums drive enforcement `[bach2010]`; supply chains diffuse labor standards only conditionally `[malesky2018]`; competitive races to the bottom in labor rights do not appear once properly tested `[guasti2022]`.

**Added after the coverage audit.** Labor rights diffuse upward through export markets `[greenhill2009]`, as does the ISO 14001 environmental standard `[prakash2006]`. Nonbinding Basel III standards still had credible distributional effects `[wilf2016]`.

**Gap.** The diffusion toolkit (spatial lags, event history) has not been applied to the *de-liberalizing* wave: investment screening, export-control regimes, data-localization and industrial-policy adoption after 2017 plausibly diffuse through the same competitor and ally channels, with security framing added. Bauerle Danzman & Meunier's mapping `[bauerle2023]` is the starting dataset.

## 17. US hegemony, the dollar and systemic power

Hegemony produces openness `[krasner1976]`, but content comes from social purpose `[ruggie1982]`; US structural power persisted `[strange1987]` and even rose as network centrality `[winecoff2020]`; the US both makes the system and takes privileges `[mastanduno2009]`, gains disproportionately `[norrlof2010]` (contested by `[drezner2013]`), and exports instability `[oatley2015]`; financial sanctions now provoke dollar hedging `[mcdowell2023]`.

**Gap.** Hegemonic-stability arguments were about public goods; weaponized interdependence turns the hegemon's position into a private good. Whether a hub state can be both system-maker and weaponizer without losing followers is the question Mastanduno's "tacit bargains" framework raises and McDowell begins to answer; a cross-national study of reserve, payment and alignment choices after 2022 would settle more.

## 18. Politicization and legitimacy of international cooperation

Multilateralism can enhance democracy `[keohane2009]` or erode representation `[gartzke2011]`; global authority generates endogenous contestation `[zurn2018]`, `[borzel2021]`; elites see IOs as more legitimate than citizens `[dellmuth2022]`; discontent matters when entrepreneurs politicize it through opportunity structures `[devries2021]`; globalization lowers pledge fulfillment `[schneider2024]`.

**Gap.** The legitimacy literature is about IOs; the legitimacy of *economic-security* policy (export controls, screening, sanctions) in democracies, and of China's institutions among followers, has no comparable survey infrastructure. A LegGov-style elite-citizen comparison on geoeconomic instruments is feasible and new.

---

## 19. Foreign aid and development finance (added after the coverage audit)

**Claimed.** Aid buys policy concessions from leaders with small winning coalitions `[bdm2009]`. Unearned foreign income lets autocrats fund patronage and survive `[ahmed2012]`, though aid tied to democratization works when autocrats expect to stay competitive after a transition `[wright2009]`.

**Settled.** Allocation is political: donors favor allies and adapt delivery to recipient governance, bypassing weak states through NGOs `[dietrich2013]`. Major donors steer multilateral development banks `[kilby2006]`, consistent with the informal-governance findings in Section 7. Donors increasingly target places whose problems spill over to them `[bermeo2017]`.

**Contested.** What Chinese aid and lending do. Chinese aid follows political alignment while its commercial lending follows economic interest `[dreher2018]`, `[dreher2022]`. Publics reward US aid more than Chinese finance with goodwill `[blair2021]`. Whether China's development finance is a rival order or a commercially driven outside option remains open (Section 7).

**Gaps and open questions.**
- *Aid in a geoeconomic contest.* US, EU (Global Gateway), Japanese and Chinese development finance now compete explicitly. No top-journal study models donor competition as strategic interaction with recipient hedging as the outcome.
- *Autocratic donors.* Cottiero & Schneider's autocratic-IFI finding `[cottiero2026]` has no bilateral counterpart. Do Gulf, Russian and Chinese bilateral flows rise when recipient autocrats face threats?
- *Aid and order alignment.* Whether aid shifts recipients' positions on contested order questions (UN votes, BRI participation, export-control alignment) is testable with geocoded project data and the alignment measures proposed in Section 11.

## Cross-cutting roadmap: where your work fits

Reading the eighteen sections together, four openings recur, each matched to assets you already have.

1. **Globalization backlash beyond the OECD.** The single largest empirical gap in Section 3, with Rudra's compensation logic (Section 2) as the theory to test. *Asset:* the Globalization Grievance Index as the dependent or mediating variable; LLM-coded grievance text as a measure that separates economic from cultural content.
2. **An open-economy-politics of economic security.** Sections 4, 9, 10 and 14 agree that the firm/preference toolkit has not been applied to export controls, screening and subsidies, and that the security-vs-protection identification problem is unsolved. *Asset:* the HS-6 dual-use classification as the product-level exposure and treatment variable; lobbying, customs and subsidy microdata as outcomes.
3. **The autocratic economic governance complex.** Sections 7, 11 and 12 show the pieces (autocratic IFIs, regional organizations, Chinese finance, authoritarian international law) but no test of whether they form an order with commitment and compensation devices, nor a standard measure of states' order alignment. *Asset:* your order-contestation project and text-as-data capacity for leader and IO speech.
4. **Measurement as contribution.** Across sections, the binding constraint is data: grievance, firm positions on controls, staff anticipation, order alignment, security motives. Validated LLM annotation with bias correction is the method IPE lacks, and a methods-plus-substance paper (measure, validate, then test a Section 9/10 hypothesis) is a credible top-journal path.

## Coverage audit and additions

The original graph was not a systematic sample. It started from your Zotero library, which over-represents your interests (LIO contestation, China, globalization backlash, *IO* and *AJPS*), plus works I judged canonical. To check that bias I pulled the 400 most-cited 2006–2026 articles from each of ten journals in Crossref (*IO, WP, APSR, AJPS, JOP, ISQ, BJPS, IS, RIPE, RIO*), filtered them to IPE topics, and compared them with the graph.

**What was added (70 works).** Investment treaties and FDI (12), the WTO and PTAs (12, including Davis & Wilf 2017 and Allee & Scalera 2012 from your library), trade and immigration attitudes (11), IMF, money and debt (12), sanctions and statecraft (7), labor and environmental standards (2), foreign aid as a new theme (8), and order, borders and polycrisis (4). Title, authors, year, venue and DOI for each new supplementary work come straight from its Crossref record. Its one-line claim is my summary and was not re-read against the paper.

**Remaining limits.**
- Citation counts favor older papers, so 2023–2026 work is still probably under-sampled. A pass through journal tables of contents for those years is the next step.
- Books and journals outside the ten checked were not audited systematically.
- The keyword filter is crude. Comparative political economy (welfare states, inequality) and resource politics were mostly left out on purpose as outside the brief.

## What I could not verify (flagged)

- Existence: 101 of the original 102 supplementary works confirmed in Crossref, and all 70 audit additions were taken from Crossref records. Colgan & Keohane 2017 (*Foreign Affairs*) is unconfirmed because the magazine is not indexed.
- Venue or year still soft: Chilton, Milner & Tingley (BJPS 2020) and Funke, Schularick & Trebesch (*European Economic Review* 2016) matched only their SSRN preprints; Mosley's *Global Capital and National Governments* is dated 2001 in Crossref but usually cited as 2003.
- Claims and edge justifications for supplementary works, including the 70 additions, are my summaries, not checked against full text this session.
- Crossref dates some articles by online-first year, so a few added works show a year one earlier than their print issue (e.g., Dür et al. 2013 for the 2014 *RIO* issue).
- Years for Han et al. (working paper), Baccini & Sattler (AJPS, c. 2024) and the IO 75th-anniversary pieces (dated 2021 here).
- The existence of a canonical, top-journal, empirical paper on economic-security policy choice for 2024-26; the searches returned special-issue introductions, working papers and policy pieces only. Treat Section 10's "settled" paragraph as provisional.
- One repo entry (`YXV7RH9E`, Mansfield, Milner & Rosendorff 2000) is coded in `papers.json` from the abstract only; its claim is correspondingly thin.
- Edge justifications are my readings of how works relate, informed by the repo analyses; where two works are contemporaneous (e.g., Weiss & Wallace and Pearson, Rithmire & Tsai; Farrell & Newman and Winecoff) the edge note says so and the direction is conventional rather than chronological.
