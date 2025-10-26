import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(ArcElement, Tooltip, Legend);

export default function SpendingPieChart({ data }) {
  // If no data yet, show loading
  if (!data || Object.keys(data).length === 0) {
    return <div>Loading spending data...</div>;
  }

  // Prepare data for Chart.js
  const chartData = {
    labels: Object.keys(data),
    datasets: [{
      label: 'Spending by Category',
      data: Object.values(data),
      backgroundColor: [
        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', 
        '#9966FF', '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0'
      ],
    }]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'bottom',
      },
      title: {
        display: true,
        text: 'Your Spending by Category'
      }
    }
  };

  return (
    <div style={{ maxWidth: '500px', margin: '20px auto' }}>
      <Pie data={chartData} options={options} />
    </div>
  );
}