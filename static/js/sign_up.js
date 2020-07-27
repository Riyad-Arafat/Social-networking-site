$(document).ready(function () {
    var days = document.getElementById("inputDay"),
    months = document.getElementById("inputMonth"),
    years = document.getElementById("inputYear"),
    month = new Array();

    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";


    if (days && month && years) {


        for (var i = 1; i <= 31; i++) {

            var x = document.createElement('option');
            if (i < 10) {
                x.innerHTML = '0' + i;
                x.value = '0' + i;
            } else {
                x.innerHTML = i;
                x.value = i;
            }

            days.appendChild(x);
        }

        for (i = 0; i <= 11; i++) {

            var x = document.createElement('option');
            if (i < 9) {

                x.value = '0' + (i + 1);
            } else {

                x.value = i + 1;
            }

            x.innerHTML = month[i];

            months.appendChild(x);
        }

        for (i = new Date().getFullYear() - 10; i >= 1900; i--) {

            var x = document.createElement('option');

            x.innerHTML = i;
            x.value = i;
            years.appendChild(x);
        }

        var $birthdayInput = $('#id_birthday');

        if ($birthdayInput.val()) {
            var x = $birthdayInput.val().split('-', 3)
            var $day = $('#inputDay'),
                $month = $('#inputMonth'),
                $year = $('#inputYear');

            $year.val(x[0]);
            $month.val(x[1]);
            $day.val(x[2]);

        }
    }
})


$('select').change(function () {
    var $day = $('#inputDay').val(),
        $month = $('#inputMonth').val(),
        $year = $('#inputYear').val(),
        $birthdayInput = $('#id_birthday');
    var $birthday;



    $birthday = $year + "-" + $month + "-" + $day;
    $birthdayInput.val($birthday)
    console.log($birthdayInput);




})