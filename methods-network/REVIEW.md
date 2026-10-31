# Political methodology, c. 1935–2026: where it went, what settled, what is open

A narrative companion to `graph.json` and `network.html` in this folder. The graph has 315 work nodes, 20 theme nodes and 353 typed relations. Each theme section follows the same order: **what was claimed → what the evidence settled → what is contested → gaps and research opportunities**. Node ids in brackets (e.g. `[rubin1974]`) point to entries in `graph.json`.

**How the works were chosen.**
- **Shared works (59):** Works already in other maps are reused. Most come from the technology map (text as data, machine learning, LLM annotation and silicon samples), the American politics map (field experiments, conjoint, ideal points, MRP) and political psychology (survey experiments and survey measurement). Others come from comparative politics (synthetic control, latent democracy, post-KKV methodology), IR and security (networks, selection bias, sensitivity analysis), REP, China and political economy.
- **Top-cited articles (130):** These come from the most-cited 2006–2026 articles in *Political Analysis* (53), *Political Science Research and Methods*, *Sociological Methods & Research* and *JASA* (only social-science and causal-inference pieces). Methods articles from AJPS, APSR, JOP, ARPS, POQ, *Perspectives on Politics*, CPS, QJPS, PRQ, JEPS, ISQ and JPR were added too.
- **Anchors (126):** Books and classic or non-indexed articles, from Fisher, Rubin, Holland and KKV to the 2020s DiD econometrics papers, LLM benchmarks and process-tracing books.

Relations are judgments of how each work's argument relates to the other's, and every relation runs from the later work to the earlier one. One-line claims for non-library works are my summaries.

---

## 1. Potential outcomes, mechanisms and sensitivity
**Claimed.** Causal effects are contrasts of potential outcomes `[rubin1974]`, `[holland1986]`; graphs offer an alternative language `[pearl2009]`. **Settled.** Identification comes before estimation `[angristpischke2009]`, `[imbensrubin2015]`, `[keele2015]`, and mediation needs sequential ignorability `[imaikeeleyamamoto2010]`, `[imaikeeletingley2011]`. **Contested.** Whether immutable traits can be causes `[senwasow2016]`; which controls help or hurt `[keele2019psrm]`, `[cinelli2022]`. **Gaps.** Sensitivity analysis is still rarely reported `[cinellihazlett2020]`, `[eggerstunon2023]`.

## 2. Regression, matching and selection on observables
**Claimed.** Propensity scores remove observed confounding `[rosenbaumrubin1983]`. **Settled.** Matching as preprocessing reduces model dependence `[hoimaiking2007]`, `[iacus2012]`, `[hainmueller2012]`. However, observational estimators often miss experimental benchmarks `[lalonde1986]`, `[arceneaux2006]`. **Contested.** Propensity-score matching itself `[kingnielsen2019]`; what regression weights `[aronowsamii2016]`. **Gaps.** Interaction models routinely extrapolate `[brambor2006]`, `[hainmuellermummoloxu2019]`.

## 3. Difference-in-differences, fixed effects and synthetic control
**Claimed.** Comparison groups stand in for counterfactual trends `[cardkrueger1994]`; synthetic units do the same for single cases `[abadie2010]`. **Settled.** Standard errors need clustering `[bertrand2004did]`, and TWFE is biased under heterogeneous, staggered effects `[dechaisemartin2020]`, `[goodmanbacon2021]`, `[imaikim2020]`. **Contested.** Which robust estimator to use `[callawaysantanna2021]`, `[liuwangxu2022]`, `[roth2023]`. **Gaps.** Dynamics and feedback in TSCS data `[blackwellglynn2018]`, `[imaikim2019]`.

## 4. Natural experiments, IV and regression discontinuity
**Claimed.** IV identifies complier effects `[imbensangrist1994]`; RD is local randomization `[hahn2001]`, `[lee2008rd]`. **Settled.** Design-based standards for natural experiments `[dunning2012]`; robust RD inference `[calonico2014]`. **Contested.** The value of local effects `[deaton2010]` vs `[imbens2010]`; close-election balance `[caugheysekhon2011]` vs `[eggers2015]`. **Gaps.** IV designs in political science are fragile `[lal2024]`.

## 5. Field experiments
**Claimed.** Randomized field interventions revive causal study of participation `[gerbergreen2000]`. **Settled.** Social pressure mobilizes `[gerber2008]`, `[bond2012]`, but campaign persuasion is near zero `[kallabroockman2018]`. **Contested.** External validity of development RCTs `[deaton2010]`, `[findley2021]`. **Gaps.** Interference and spillovers `[bowers2013]`, `[aronowsamii2017]`; multi-site replication `[dunning2016]`.

## 6. Survey experiments and generalizability
**Claimed.** Population-based survey experiments combine internal and external validity `[mutz2011]`. **Settled.** Convenience samples often reproduce national effects `[mullinix2015]`, `[coppock2018]`, and demand effects are small `[mummolopeterson2019]`. **Contested.** Pretreatment, spillover and information-equivalence problems `[gaineskuklinski2007]`, `[dafoe2018]`. **Gaps.** Formal frameworks for external validity `[egamihartman2023]`.

## 7. Conjoint, list and sensitive-question designs
**Claimed.** Indirect questions reveal hidden attitudes `[warner1965]`, `[kuklinski1997]`. **Settled.** Conjoints identify AMCEs `[hhy2014]`, and list experiments have multivariate estimators `[blairimai2012]`. **Contested.** What AMCEs mean `[leeper2020]`, `[abramson2022]`, `[delacuesta2021]`; how large sensitivity bias is `[blaircoppockmoor2020]`. **Gaps.** Validation against behavior `[rosenfeld2016]`.

## 8. Ideal points and spatial scaling
**Claimed.** Roll calls reveal low-dimensional ideal points `[poolerosenthal1985]`. **Settled.** Bayesian IRT gives the same scores with uncertainty `[clinton2004]`, `[martinquinn2002]`. Bridging puts different institutions on one scale `[bailey2007]`, `[shormccarty2011]`. **Contested.** What new data sources measure, such as donations, likes and follows `[bonica2014]`, `[bondmessing2015]`, `[barbera2015]`. **Gaps.** Scaling massive and multilingual data `[imai2016]`.

## 9. Concepts, measurement and latent variables
**Claimed.** Concepts must not be stretched `[sartori1970]`, `[collierlevitsky1997]`. **Settled.** Measurement validity is a shared standard `[adcockcollier2001]`, and latent-variable models give scores with uncertainty `[treierjackman2008]`, `[pemstein2010]`, `[fariss2014]`. **Contested.** Aggregation of democracy indices `[munckverkuilen2002]`, `[coppedge2011]`. **Gaps.** Validating familiar survey measures `[bauer2016]`, `[druckmanlevendusky2019]`.

## 10. Text as data
**Claimed.** Words can be treated as data to scale texts `[laver2003]`, `[slapinproksch2008]`. **Settled.** Topic models measure attention `[quinn2010]`, `[robertsstm2014]`. Methods must be validated `[grimmerstewart2013]`. **Contested.** Preprocessing sensitivity `[dennyspirling2018]`; embeddings `[rheaultcochrane2019]`, `[rodriguezspirling2022]`. **Gaps.** Causal inference with text `[egami2022]`; low-resource classification `[laurer2023]`.

## 11. Machine learning and heterogeneous effects
**Claimed.** Prediction is its own culture `[breiman2001]`. **Settled.** Forests and ensembles estimate heterogeneous effects with valid inference `[wagerathey2018]`, `[kunzel2019]`, `[chernozhukov2018]`. **Contested.** Prediction vs explanation in conflict research `[wardgreenhill2010]`, `[muchlinski2016]`. **Gaps.** Learned proxies in causal tests `[knox2022]`.

## 12. LLMs for annotation, measurement and simulation
**Claimed.** LLMs annotate as well as crowd workers or experts `[gilardi2023]`, `[tornberg2024]` and can simulate respondents `[argyle2023]`. **Settled.** Zero-shot performance is strong but uneven across tasks `[ziems2024]`, `[halterman2025]`. **Contested.** Silicon samples `[bisbee2024]`, `[dillion2023]`; closed models and reproducibility `[spirling2023]`. **Gaps.** Bias-corrected downstream inference with LLM labels `[egami2025]`; LLM-based scaling `[lemens2025]`, `[benoit2026]`; qualitative coding `[than2025]`.

## 13. Bayesian and multilevel models
**Claimed.** Multilevel models fit clustered political data `[steenbergenjones2002]`. **Settled.** MRP estimates small-area opinion `[park2004]`, `[laxphillips2009ajps]`, even from unrepresentative polls `[wang2015]`. **Contested.** Few-cluster inference `[stegmueller2013]`. **Gaps.** Dynamic group-level IRT `[caugheywarshaw2015]`.

## 14. Time-series cross-section and dynamic models
**Claimed.** OLS with panel-corrected standard errors `[beckkatz1995]`; binary TSCS data are duration data `[beckkatztucker1998]`. **Settled.** Dynamics should be modeled explicitly `[deboefkeele2008]`, `[beckkatz2011]`. **Contested.** Fixed versus random effects `[greenkimyoon2001]`, `[belljones2014]`; lagged variables `[keelekelly2006]`, `[bellemare2017]`. **Gaps.** A causal reading of TSCS models `[blackwellglynn2018]`.

## 15. Missing data and imputation
**Claimed.** Ignorability conditions for missing data `[rubin1976]`. **Settled.** Multiple imputation beats listwise deletion in most settings `[king2001]`, `[honakerking2010]`, `[lall2016]`. **Contested.** When deletion is fine `[pepinsky2018]`. **Gaps.** Measurement error as missing data `[blackwellhonakerking2017]`; scalable imputation `[lallrobinson2021]`.

## 16. Survey methodology and sampling
**Claimed.** Answers are constructed on the spot `[zallerfeldman1992]`; respondents satisfice `[krosnick1991]`. **Settled.** Nonresponse rates are weak predictors of bias `[groves2006]`, and misreporting inflates turnout `[ansolabeherehersh2012]`. **Contested.** Nonprobability samples `[macinnis2018]` vs `[ansolabehereschaffner2014]`. **Gaps.** Online-panel data quality `[kennedy2020]`; polling errors `[kennedy2018]`.

## 17. Qualitative and multi-method research
**Claimed.** One logic of inference for all research `[king1994]`. **Settled.** Causal-process observations and process tracing have their own leverage `[bradycollier2004]`, `[georgebennett2005]`, `[collier2011]`. **Contested.** Two cultures `[mahoneygoertz2006]`; set-theoretic QCA `[ragin2008]`; mechanisms `[gerring2010]`. **Gaps.** Bayesian integration `[humphreysjacobs2015]`, `[fairfieldcharman2017]`, `[humphreysjacobs2023]`.

## 18. Formal models and EITM
**Claimed.** Rational choice lacks empirical tests `[greenshapiro1994]`. **Settled.** Formal models can be estimated and tested `[signorino1999]`, `[morton1999]`, `[granato2004]`. **Contested.** Whether models should be tested at all `[clarkeprimo2012]`; formal models of autocracy `[przeworski2022]`. **Gaps.** Matching estimands to theory `[bdmtyson2020]`, `[ashworth2021]`.

## 19. Replication, transparency and preregistration
**Claimed.** Replication standards `[king1995]`; most findings may be false `[ioannidis2005]`. **Settled.** Publication bias exists `[gerbermalhotra2008qjps]`, `[franco2014]`, and researcher degrees of freedom inflate false positives `[simmons2011]`, `[osc2015]`. **Contested.** DA-RT for qualitative research `[monroe2018]`, `[jacobs2021]`. **Gaps.** Design declaration `[blair2019]`; undisclosed specification choices `[lenzsahn2020]`.

## 20. Networks and spatial interdependence
**Claimed.** Peer effects are hard to identify `[manski1993]`. **Settled.** Spatial and network dependence must be modeled `[beck2006isq]`, `[franzesehays2007]`, `[hoffward2004]`, `[cranmerdesmarais2011]`. **Contested.** Observational contagion `[christakisfowler2007]` vs `[shalizithomas2011]`. **Gaps.** Experimental designs for spillovers `[bond2012]`, `[aronowsamii2017]`.

---

## What I could not verify (flagged)
Every anchor and library seed (125) was checked in Crossref: 113 matched directly. 6 books exist in Crossref only through reviews or chapters about them: Brady 2004, Brown 2020, Gerber 2012, Grimmer 2022, Open Science Collaboration 2015, Przeworski 1970. 6 were not found as their own Crossref record, so their metadata comes from memory: Achen 2002, Budge 2001, Fisher 1935, LaLonde 1986, Mikolov 2013, Rosenbaum 2002.
