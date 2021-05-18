export default function cleanSet(set, startString) {
  const rslt = [];
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  for (const i of set) {
    rslt.push(i.substr(i.length - startString.length));
  }
  return rslt.join('-');
}
