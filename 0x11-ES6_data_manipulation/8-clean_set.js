export default function cleanSet(set, startString) {
  const list = [];
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  for (const i of set) {
    list.push(i.substr(i.length - 3));
  }
  return list.join('-');
}
