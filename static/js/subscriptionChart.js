

const ctx1 = document.getElementById('subscriptions-chart').getContext('2d');
const subscriptonsChart = new Chart(ctx1, {
    type: 'bar',
    data: {

        labels: ['Total Subscriptions', 'Active Subscriptions'],
        datasets: [{
            label: 'Subscriptions',
             data: [totalSubscriptions, activeSubscriptions],

            backgroundColor: [
                '#0d6efd',
                '#00C851',
               
            ],
            borderColor: [
                '#0d6efd',
                'rgba(23, 255, 23, 0.2)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        responsive:true
    }
});
