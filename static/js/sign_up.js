var days = document.getElementById("id_birth_day"),
    months = document.getElementById("id_birth_month"),
    years = document.getElementById("id_birth_year"),
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

if ( days != null){




    for (i = 1; i <= 31; i++){

        var x = document.createElement('option');
        x.innerHTML = i;
        x.value = i;
        days.appendChild(x);
    }


    for (i = 0; i <= 11; i++){

        var x = document.createElement('option');

        x.innerHTML = month[i];
        x.value = i;
        months.appendChild(x);
    }


    for (i = new Date().getFullYear() - 10; i >= 1900; i--){

        var x = document.createElement('option');

        x.innerHTML = i;
        x.value = i;
        years.appendChild(x);
    }


}
