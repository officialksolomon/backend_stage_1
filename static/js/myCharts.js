const ctx = document.getElementById('myChart1').getContext('2d');
const myChart1 = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Total Subscriptions', 'Active Subscription'],
        datasets: [{
            label: 'Subscriptions',
            data: [totalSubscriptions == 0 ? 1:totalSubscriptions, activeSubscriptions],

            backgroundColor: [
                '#ff4444',
                '#00C851',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
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

const ctx2 = document.getElementById('myChart2').getContext('2d');
const myChart2 = new Chart(ctx2, {
    type: 'line',
    data: {

        labels: ['Prop Firm Account', 'Account Management'],
        datasets: [{
            label: 'Plans',
            data: [accountManagementPlans,propFirmPlans],

            backgroundColor: [
                '#ff4444',
                '#00C851',
               
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
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
