export default function getStudentsByLocation(obj, elemnt) {
  let rslt = [];
  try {
    rslt = obj.filter((val) => val.location === elemnt);
  } catch (e) {
    // pass
  }
  return rslt;
}
