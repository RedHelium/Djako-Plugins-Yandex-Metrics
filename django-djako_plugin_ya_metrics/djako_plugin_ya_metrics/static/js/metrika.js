$(document).ready(function() {

    
    $.ajax({
        url: '/api/v1/metrika/counter/',
        method: 'post',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        dataType: 'json',
        data: {"ya-metrika-counter": "97176187"},
        success: function(data){

            for(var index = 0; index < data["widgets"].length; index++) {
              
              const ctx = document.getElementById(data["widgets"][index]["id_chart"]);

              var chartData = {
                labels: data["widgets"][index]["labels"],
                datasets: []
              };

              for(var index_dataset = 0; index_dataset < data["widgets"][index]["datasets"].length; index_dataset++) {

                var current_dataset = data["widgets"][index]["datasets"][index_dataset];

                var dataset = {
                  label: current_dataset["dataset"]["header"],
                  data: current_dataset["dataset"]["values"],
                  borderWidth: current_dataset["dataset"]["borderWidth"],
                  fill: current_dataset["dataset"]["fill"],
                  lineTension: current_dataset["dataset"]["lineTension"]
                      
                };

                chartData.datasets.push(dataset);
              }              

              new Chart(ctx, {
                type: 'line',
                data: chartData,
                options: {
                  scales: {
                    y: {
                      beginAtZero: true
                    }
                  },
                  plugins: {
                    // title: {
                    //   display: true,
                    //   text: data["widgets"][index]["total"],
                    // }
                  }
                }
              });

            }

            }
    });
    
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}