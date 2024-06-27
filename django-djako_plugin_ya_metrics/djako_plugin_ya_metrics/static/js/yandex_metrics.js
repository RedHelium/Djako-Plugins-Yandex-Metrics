$(document).ready(function() {

    
    $.ajax({
        url: '/api/v1/djako/yandex/metrics/counter/',
        method: 'post',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        dataType: 'json',
        success: function(data){

            if(data["error"] != null) {
              $("#metrics-errors").text(data["error"]);
              return;
            }

            for(var index_counter = 0; index_counter < data["counters"].length; index_counter++) {

              var current_counter = data["counters"][index_counter]["counter"];

              for(var index = 0; index < current_counter["widgets"].length; index++) {
                
                var current_widgets = current_counter["widgets"][index];

                var ctx = document.getElementById(current_widgets["id_chart"]);

                var chartData = {
                  labels: current_widgets["labels"],
                  datasets: []
                };

                for(var index_dataset = 0; index_dataset < current_widgets["datasets"].length; index_dataset++) {

                  var current_dataset = current_widgets["datasets"][index_dataset];

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
                  type: current_widgets["chart_type"],
                  data: chartData,
                  options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                      y: {
                        beginAtZero: true
                      }
                    },
                    plugins: {
                      title: {
                        display: true,
                        text: current_widgets["title"],
                      }
                    },
                    elements: {
                      } 
                    }
                  });
                }
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