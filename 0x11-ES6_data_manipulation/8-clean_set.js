export default function cleanSet(set, startString) {
  const rslt = [];
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  for (const i of set) {
    if (i.startsWith(startString)) rslt.push(i.replace(startString, ''));
  }
  return rslt.join('-');
}
