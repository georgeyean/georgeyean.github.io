/* My Reading List: saved works shared by every LitNet page on this site.
   Stored in this browser only (localStorage), so it stays on this device and is never sent anywhere. */
(function () {
  const KEY = 'litnet-reading-list';
  const STATUSES = ['to read', 'reading', 'read'];
  const subs = [];

  function load() {
    try { const a = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(a) ? a : []; }
    catch (e) { return []; }
  }
  function save(a) {
    try { localStorage.setItem(KEY, JSON.stringify(a)); } catch (e) {}
    subs.forEach(f => { try { f(a); } catch (e) {} });
  }
  window.addEventListener('storage', e => { if (e.key === KEY) subs.forEach(f => f(load())); });

  function mergeFields(a, b) {
    const out = (a || []).slice();
    (b || []).forEach(f => { if (!out.some(x => x.dir === f.dir)) out.push(f); });
    return out;
  }

  window.ReadingList = {
    STATUSES,
    all: load,
    ids: () => new Set(load().map(x => x.id)),
    get: id => load().find(x => x.id === id),
    has: id => load().some(x => x.id === id),
    add(item) {
      const a = load();
      const ex = a.find(x => x.id === item.id);
      if (ex) ex.fields = mergeFields(ex.fields, item.fields);
      else a.push(Object.assign({ status: 'to read', added: new Date().toISOString().slice(0, 10), note: '' }, item));
      save(a);
    },
    remove(id) { save(load().filter(x => x.id !== id)); },
    toggle(item) { if (this.has(item.id)) this.remove(item.id); else this.add(item); },
    setStatus(id, s) { const a = load(); const x = a.find(x => x.id === id); if (x && STATUSES.includes(s)) { x.status = s; save(a); } },
    setNote(id, note) { const a = load(); const x = a.find(x => x.id === id); if (x) { x.note = String(note || '').slice(0, 2000); save(a); } },
    replaceAll(arr) { if (Array.isArray(arr)) save(arr.filter(x => x && x.id && x.title)); },
    clear() { save([]); },
    onChange(f) { subs.push(f); },
  };
})();
