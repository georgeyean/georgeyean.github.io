/* Abstract and official link for a work, read from <field>/abstracts.json
   (built from the Zotero library, OpenAlex, Semantic Scholar and Crossref). Used by the LitNet details panels. */
(function () {
  const cache = {};
  const css = document.createElement('style');
  css.textContent = [
    'a.title-link{color:inherit;text-decoration:none;border-bottom:1px solid rgba(46,186,174,.45)}',
    'a.title-link:hover{color:var(--accent);border-bottom-color:var(--accent)}',
    'a.title-link .ext-ic{font-size:.8em;color:var(--accent);white-space:nowrap}',
    '.abs{font-size:13.5px;line-height:1.6;margin:6px 0 2px}',
    '.abs.clamp{display:-webkit-box;-webkit-line-clamp:8;-webkit-box-orient:vertical;overflow:hidden}',
    '.abs.none{color:var(--muted);font-style:italic}',
    'button.abs-more{height:24px;line-height:24px;padding:0 10px;font-size:9px;margin-top:4px}',
    '.abs-src{font-size:11.5px;color:var(--muted);margin-top:4px}',
  ].join('\n');
  document.head.appendChild(css);

  function load(dirUrl) {
    return cache[dirUrl] || (cache[dirUrl] = fetch(dirUrl + '/abstracts.json').then(r => (r.ok ? r.json() : {})).catch(() => ({})));
  }
  function link(w, e) {
    if (e && e.u) return { href: e.u, official: true };
    const doi = w.crossref_doi || w.doi;
    if (doi) return { href: 'https://doi.org/' + doi, official: true };
    const first = (w.authors || '').split(/,| & /)[0];
    return { href: 'https://scholar.google.com/scholar?q=' + encodeURIComponent('"' + w.title + '" ' + first), official: false };
  }
  // fill: d3 selection (an empty container) that gets the linked title
  function title(box, w, e) {
    const l = link(w, e);
    box.html('').append('p').attr('class', 'title').append('a').attr('class', 'title-link').attr('href', l.href)
      .attr('target', '_blank').attr('rel', 'noopener')
      .attr('title', l.official ? 'Open the official page' : 'No official page found: search Google Scholar')
      .text(w.title).append('span').attr('class', 'ext-ic').text(' ↗');
  }
  function abstract(box, e) {
    box.html('');
    box.append('div').attr('class', 'lbl').text('Abstract');
    if (!e || !e.a) { box.append('p').attr('class', 'abs none').text('No abstract found.'); return; }
    const p = box.append('p').attr('class', 'abs').text(e.a);
    if (e.a.length > 650) {
      p.classed('clamp', true);
      const b = box.append('button').attr('type', 'button').attr('class', 'abs-more').text('Show full abstract')
        .on('click', () => { const c = p.classed('clamp'); p.classed('clamp', !c); b.text(c ? 'Show less' : 'Show full abstract'); });
    }
    box.append('div').attr('class', 'abs-src').text('Abstract via ' + e.s);
  }
  window.PaperInfo = { load, link, title, abstract };
})();
