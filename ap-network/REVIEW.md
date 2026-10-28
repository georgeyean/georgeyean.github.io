# American politics, c. 1957–2026: where it went, what settled, what is open

A narrative companion to `graph.json` and `network.html` in this folder. The graph has 385 work nodes, 18 theme nodes and 415 typed relations. Each theme section follows the same order: **what was claimed → what the evidence settled → what is contested → gaps and research opportunities**. Node ids in brackets (e.g. `[mayhew1974]`) point to entries in `graph.json`.

**How the works were chosen.**
- **Your library:** three American-politics entries in `papers.json` are seeded directly: Enos & Hersh on campaign ground workers, Bailey et al. on courts and LGBTQ media, and Kuk, Seligsohn & Zhang on Congress after the China shock.
- **Shared works:** 21 works already in the IPE, security, IR, comparative and China maps are imported unchanged. Examples include Graham & Svolik, Autor et al., Mutz, Hainmueller & Hiscox and Levitsky & Ziblatt.
- **Top-cited articles:** 281 come from the 400 most-cited 2006–2026 articles in eleven American-politics journals plus *APSR*, *AJPS*, *JOP* and the *Annual Review*. The eleven are *Public Opinion Quarterly*, *Political Behavior*, *Legislative Studies Quarterly*, *Political Research Quarterly*, *American Politics Research*, *Presidential Studies Quarterly*, *Political Psychology*, *Perspectives on Politics*, *Political Communication*, *State Politics & Policy Quarterly* and *Studies in American Political Development*. Their metadata comes from Crossref.
- **Anchors:** 80 books and classic articles, from Downs, *The American Voter* and Mayhew through Mason, Sides–Tesler–Vavreck and Kalmoe & Mason. Each was checked in Crossref; see "What I could not verify" below.

One-line claims for non-library works are my summaries, not re-read this session. I left out pure survey methodology and causal-inference methods papers, which dominate citation counts in *POQ*, *AJPS* and *JOP* but are not substantive American politics.

---

## 1. Elite and mass polarization

**Claimed.** Roll-call voting is low-dimensional and Congress has polarized steadily since the 1970s `[poolerosenthal1997]`, tracking inequality and immigration `[mccarty2006]`. The mass public, by contrast, is sorted but not polarized `[fiorina2005]`.

**Settled.** Elite polarization is real and asymmetric over time. It reaches state legislatures `[shormccarty2011]` and is now nationalized `[hopkins2022]`. Gerrymandering is not the main cause `[mccarty2009]`. Members leapfrog their median voters `[bafumiherron2010]`, and extremist primary winners cost their party votes `[hall2015]`.

**Contested.** How polarized the public is:
- the engaged public is polarized `[abramowitz2008]`, `[abramowitz2010]`;
- it is sorting, not divergence `[fiorinaabrams2008]`, `[fiorina2008]`;
- many voters follow party over ideology `[barberpope2019]`.

Mechanisms also compete. Candidate supply `[thomsen2014]`, donors `[barber2016jop]`, `[bonica2014]`, team play `[leesenate2009]`, `[lee2016]` and trade shocks `[autor2020]`, `[kuk2022]` all have support.

**Gaps.** Measures of elite ideology rest on roll calls and money. Speeches, press releases and social media posts scaled with validated LLMs could separate ideology from partisan team play, which roll calls cannot.

## 2. Partisan identity and affective polarization

**Claimed.** Party identification is a stable social identity `[campbell1960]`, `[greenpalmquist2002]`, not a running tally of performance `[fiorina1981]`.

**Settled.** Partisans increasingly dislike the other side `[iyengar2012]`, `[iyengarwestwood2015]`, `[iyengar2019]`. Sorting of identities intensifies anger even without issue extremity `[mason2015]`, `[mason2018]`. Partisanship shapes dating `[hubermalhotra2017]`, hiring and pay `[mcconnell2018]` and economic behavior `[gerberhuber2009]`.

**Contested.** Whether affect is ideological `[websterabramowitz2017]`, `[rogowskisutherland2016]` or purely social `[iyengar2012]`. How much measures overstate it `[druckmanlevendusky2019]`, `[druckman2022]`. Whether it actually harms behavior `[lelkeswestwood2017]`.

**Gaps.** Interventions reduce affect `[levendusky2018]`, `[wojcieszakwarner2020]`, but few studies show they change downstream democratic attitudes, a link `[kingzette2021]` suggests is the one that matters.

## 3. Opinion formation: framing, cues and motivated reasoning

**Claimed.** Mass belief systems lack constraint `[converse1964]`, and opinion follows elite messages filtered by awareness `[zaller1992]`. Collective opinion is nonetheless stable and sensible `[pageshapiro1992]`.

**Settled.** Framing effects are real but conditional on frame strength, competition and timing `[chongdruckman2007arps]`, `[chongdruckman2007]`, `[chongdruckman2010]`. People reason in motivated ways `[taberlodge2006]`, `[lodgetaber2013]`. Party cues shape opinion and value expression `[goren2009]`, `[slothuusdevreese2010]`.

**Contested.** How much cues dominate content:
- policy information matters as much as cues `[bullock2011]`, `[boudreaumackenzie2014]`;
- elite polarization strengthens cues `[druckman2013]`;
- apparent priming is often learning `[lenz2009]`, `[tesler2015]`.

Measurement error may explain apparent incoherence `[ansolabehere2008]`.

**Gaps.** Most evidence comes from one-shot survey experiments, and pretreatment mutes effects `[druckmanleeper2012]`. Panel designs that follow real information flows remain rare.

## 4. Misinformation, conspiracy beliefs and fact-checking

**Claimed.** Corrections fail and can backfire `[nyhanreifler2010]`.

**Settled.** Backfire is rare, and corrections generally improve accuracy `[woodporter2019]`, `[walter2020]`. But they rarely change attitudes or votes `[nyhan2020]`, and belief echoes persist `[thorson2016]`. Exposure to and sharing of fake news is concentrated in small groups `[allcottgentzkow2017]`, `[guess2019]`.

**Contested.** Motivated reasoning versus inattention `[pennycookrand2019]`, `[osmundsen2021]`. Whether social media causes conspiracy belief or only activates predispositions `[enders2021]`, `[uscinski2016]`.

**Gaps.** Work centers on Twitter and Facebook before 2022. Generative AI content and closed messaging apps are understudied.

## 5. News media, selective exposure and social media

**Claimed.** Media choice fragments audiences and polarizes `[sunstein2001]`, `[prior2007]`.

**Settled.** Partisan media persuade `[dellavignakaplan2007]`, `[martinyurukoglu2017]`, and slant follows demand `[gentzkowshapiro2010]`. Local news decline nationalizes politics and lowers engagement `[martinmccrain2019]`, `[moskowitz2021]`, `[hayeslawless2018]`.

**Contested.** Echo chambers: most people have moderate diets `[guess2021]`, `[flaxman2016]`, and individual choice matters more than algorithms `[bakshy2015]`. Cross-cutting exposure can even polarize `[bail2018]`. Effects of partisan media may concentrate among extremes `[levendusky2013]`, `[prior2013]` or spread through discussion `[druckman2018]`.

**Gaps.** Platform data access has collapsed since 2023. Research on video platforms and podcasts is thin.

## 6. Turnout, mobilization and participation

**Claimed.** Voting is irrational on cost-benefit grounds `[downs1957]`. Participation depends on resources and recruitment `[verba1995]`, `[rosenstonehansen1993]`.

**Settled.** Field experiments transformed this area. Canvassing works `[gerbergreen2000]`, social pressure works strongly `[gerber2008]`, and effects spill over within households `[nickerson2008]`. Participation is partly heritable `[fowler2008]`.

**Contested.** Voter ID effects:
- reduce minority turnout `[hajnal2017]`;
- no effect in voter-file panels `[cantonipons2021]`.

Whether education causes participation `[kampalmer2008]`, `[berinskylenz2011]`.

**Gaps.** Most experiments come from low-salience elections and may not scale to presidential contests.

## 7. Campaigns, elections and accountability

**Claimed.** Voters judge incumbents retrospectively `[fiorina1981]`, and members seek reelection `[mayhew1974]`.

**Settled.** Retrospection is myopic `[healymalhotra2009]`, `[healylenz2014]` and responds to irrelevant events `[achenbartels2016]`. Campaign persuasion in general elections is near zero `[kallabroockman2018]`, and ad effects decay fast `[gerber2011]`. The incumbency advantage has declined `[jacobson2015]`.

**Contested.** Economic versus identity explanations of 2016:
- trade shocks moved votes `[autor2020]`, `[jensen2017]`, `[baccini2021]`;
- status threat and racial attitudes did `[mutz2018]`, `[sides2018]`, `[reny2019]`.

**Gaps.** Campaign data and targeting `[hersh2015]`, `[enoshersh2015]` are now driven by private firms whose effects are hard to observe.

## 8. Race, ethnicity and immigration

**Claimed.** Racial resentment structures white opinion `[kindersanders1996]`, implicit appeals activate it `[mendelberg2001]`, and linked fate anchors Black politics `[dawson1994]`.

**Settled.** Obama's presidency racialized many issues `[tesler2012]`, `[tesler2016]`. Explicit racial rhetoric no longer triggers backlash `[valentino2018]`. Legislators discriminate in responsiveness `[butlerbroockman2011]`. Slavery's legacy persists in Southern attitudes `[acharya2016]`.

**Contested.** Immigration attitudes rest on cultural threat `[brader2008]`, `[hainmuellerhopkins2015]` versus local economic shocks `[malhotra2013]` and context `[hopkins2010]`. Protest effects depend on violence `[wasow2020]`, `[enos2019]`, `[renynewman2021]`.

**Gaps.** Latino and Asian American politics `[hajnallee2011]`, `[kuo2017]` remains thin relative to its electoral weight, especially Latino shifts toward Republicans after 2016.

## 9. Gender and political representation

**Claimed.** Women are underrepresented because they do not run, not because voters discriminate `[lawlessfox2010]`.

**Settled.** The ambition gap starts early `[foxlawless2014]` and recruitment matters `[foxlawless2010]`. Women who win are effective `[anziaberry2011]`, `[volden2013]`. Voters show a slight average preference for women `[schwarzcoppock2022]`.

**Contested.** Demand-side bias: a double bind for mothers `[teele2018]` and sexism in 2016 `[valentino2018poq]`, `[cassesebarnes2019]`.

**Gaps.** The partisan gap, with few Republican women `[thomsen2015]`, deserves more causal work.

## 10. Representation, responsiveness and inequality

**Claimed.** Policy follows opinion `[stimson1995]`, `[erikson1993]`.

**Settled.** Responsiveness is unequal by income `[bartels2008]`, `[gilens2012]`. State policy matches majority opinion only about half the time `[laxphillips2012]` and responds slowly `[caugheywarshaw2018]`. Elites misperceive constituents as more conservative `[broockmanskovron2018]`, `[hertelfernandez2019apsr]`.

**Contested.** Whether average citizens have independent influence `[gilenspage2014]`. Critics argue that rich and middle-class preferences rarely diverge, so the effect is hard to identify.

**Gaps.** Working-class underrepresentation `[carnes2012]`, `[carneslupu2016]` connects inequality to who runs, a supply side still underexplored.

## 11. Congress, parties and legislative behavior

**Claimed.** Parties are procedural cartels `[coxmccubbins2005]`. Pivots explain lawmaking `[krehbiel1998]`. Parties are coalitions of policy demanders `[bawn2012]`.

**Settled.** Majorities control the floor `[finocchiarorohde2008]`. Lobbyists subsidize allies `[halldeardorff2006]`. Members choose credit claiming or position taking by district `[grimmer2013book]`.

**Contested.** Party loyalty costs votes `[carson2010]`, yet partisan conflict is rewarded by strong partisans `[harbridgemalhotra2011]`.

**Gaps.** Congress's declining capacity (staff, committees) and its effect on policy expertise are understudied.

## 12. Presidency, bureaucracy and executive power

**Claimed.** Presidents persuade `[neustadt1960]`, go public `[kernell1986]` or act unilaterally `[moehowell1999]`, `[howell2003]`.

**Settled.** Unilateral tools are widely used `[rudalevige2012]`, `[lowande2014]`. Presidents steer spending to supporters `[berry2010]`, `[larcinese2006]`. Appointees can lower agency performance `[lewis2007]`, `[lewis2008]`.

**Contested.** How much public opinion constrains unilateralism `[reevesrogowski2015]`. Whether the presidency is becoming a strongman office `[howellmoe2023]`.

**Gaps.** Second-term Trump-era actions such as impoundment, firings and Schedule F are not yet in the citation record.

## 13. Courts and judicial politics

**Claimed.** Justices vote preferences `[segalspaeth2002]` but strategically `[epsteinknight1998]`. Courts rarely cause social change `[rosenberg1991]`.

**Settled.** Judge identity affects decisions `[boyd2010]`, `[glynnsen2015]`, `[kastellec2013]`. Court legitimacy is fairly durable `[gibsonnelson2014]`.

**Contested.** Whether ideological disagreement erodes legitimacy `[bartelsjohnston2013]`, `[christensonglick2015]`. Whether rulings shape public attention `[bailey2024]`.

**Gaps.** Legitimacy work largely predates the post-Dobbs collapse in confidence.

## 14. Interest groups, lobbying and money

**Claimed.** The pressure system has an upper-class bias `[schattschneider1960]`.

**Settled.** Donors buy access `[kallabroockman2016]`. Contribution data scale ideology `[bonica2014]`. Organized conservative networks reshape states `[hertelfernandez2019]`, `[skocpolhertel2016]`.

**Contested.** Whether lobbying moves outcomes: mostly not `[baumgartner2009]`, or yes for business `[gilenspage2014]`, `[richter2009]`.

**Gaps.** Firm-level lobbying `[kim2017]` links to your IPE work, but domestic regulatory lobbying data remain limited.

## 15. States, localities and policy diffusion

**Claimed.** States innovate and emulate `[walker1969]`, `[berryberry1990]`.

**Settled.** Diffusion runs through learning, competition, imitation and coercion `[shipanvolden2008]`. Partisan control matters incrementally `[caughey2017]`. MRP made state opinion measurable `[laxphillips2009ajps]`.

**Contested.** Whether mayoral partisanship matters `[gerberhopkins2011]`, `[debenedictis2016]`.

**Gaps.** Nationalization of state politics `[hopkins2022]` may be eroding the laboratories-of-democracy model.

## 16. Policy feedback and American political development

**Claimed.** Policies remake politics `[pierson1993]`.

**Settled.** Social Security mobilized seniors `[campbell2003]`. Submerged policies hide government `[mettler2011]`. The carceral state demobilizes citizens `[weaverlerman2010]`.

**Contested.** Liberal reforms often fail to build feedback `[patashnikzelizer2013]`. Feedback is conditional on experience `[lermanmccabe2017]`.

**Gaps.** Long-run feedback from the ACA and pandemic-era programs is open.

## 17. Democratic norms, populism and backsliding

**Claimed.** Democracies die when parties abandon forbearance `[levitskyziblatt2018]`.

**Settled.** Partisans trade democratic principles for party `[grahamsvolik2020]`, `[svolik2019]`. Ethnic antagonism predicts antidemocratic views `[bartels2020]`.

**Contested.** How widespread support for political violence is `[kalmoemason2022]`, given measurement concerns. Cultural versus economic roots of populism `[inglehartnorris2017]`, `[han2024]`.

**Gaps.** Elite behavior after 2020, including election administrators and state officials, needs more study.

## 18. Personality, emotion, values and genes

**Claimed.** Emotion guides judgment `[marcus2000]`, and attitudes are partly heritable `[alford2005]`.

**Settled.** Big Five traits predict ideology `[gerber2010]`. Anxiety drives information seeking `[valentino2008]`, and anger drives participation `[valentino2011]`.

**Contested.** Ideological asymmetries `[jost2017]` and the direction of moral foundations `[smith2017]`.

**Gaps.** Genetic findings `[fowlerdawes2008]` have largely failed to replicate.

---

## Cross-cutting roadmap: where your work fits

1. **Trade, identity and polarization.** The China shock, Congress and populism link `[autor2020]`, `[kuk2022]`, `[ballardrosa2024]` and `[han2024]`. This connects the American politics map to your IPE map.
2. **Text as data for elites.** Validated LLM annotation of congressional speech, press releases and executive actions could measure ideology, team play and unilateralism beyond roll calls.
3. **Backsliding in comparative perspective.** American backsliding work `[grahamsvolik2020]` connects to your autocracy interests and the comparative map.

## What I could not verify (flagged)

- **Anchors:**
  - 80 anchors were checked in Crossref. 57 matched on title and author.
  - 22 were found only through published reviews, chapters or catalog records.
  - Sunstein's *Republic.com* (2001) is not in Crossref, though its 2017 sequel is.
- **Library entries:** Kuk, Seligsohn & Zhang appeared in *Economics & Politics* in 2022 after a 2018 SSRN version.
- **Claims:** one-line claims and edge justifications for non-library works are my summaries, not checked against full text.
- **Coverage:**
  - Citation counts favor 2006–2015 work, so post-2020 research is underrepresented.
  - Methods papers were excluded.
  - Books are central in American politics and are covered only through selected anchors.
