export const weakMap = new WeakMap();

export default function queryAPI(endpoint) {
    let i = weakMap.get(endpoint);
    if (i !== undefined) weakMap.set(endpoint, i++);
    if (weakMap.get(endpoint) >= 5) throw Error('Endpoint load is high');
}