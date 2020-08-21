$(document).ready(function() {
    var e = document.getElementById("inputDay"),
        n = document.getElementById("inputMonth"),
        t = document.getElementById("inputYear"),
        a = new Array;
    if (a[0] = "January", a[1] = "February", a[2] = "March", a[3] = "April", a[4] = "May", a[5] = "June", a[6] = "July", a[7] = "August", a[8] = "September", a[9] = "October", a[10] = "November", a[11] = "December", e && a && t) {
        for (var r = 1; r <= 31; r++) {
            var l = document.createElement("option");
            r < 10 ? (l.innerHTML = "0" + r, l.value = "0" + r) : (l.innerHTML = r, l.value = r), e.appendChild(l)
        }
        for (r = 0; r <= 11; r++) {
            (l = document.createElement("option")).value = r < 9 ? "0" + (r + 1) : r + 1, l.innerHTML = a[r], n.appendChild(l)
        }
        for (r = (new Date).getFullYear() - 10; r >= 1900; r--) {
            (l = document.createElement("option")).innerHTML = r, l.value = r, t.appendChild(l)
        }
        var i = $("#id_birthday");
        if (i.val()) {
            l = i.val().split("-", 3);
            var u = $("#inputDay"),
                o = $("#inputMonth");
            $("#inputYear").val(l[0]), o.val(l[1]), u.val(l[2])
        }
    }
}), $("select").change(function() {
    var e, n = $("#inputDay").val(),
        t = $("#inputMonth").val(),
        a = $("#inputYear").val(),
        r = $("#id_birthday");
    e = a + "-" + t + "-" + n, r.val(e), console.log(r)
});