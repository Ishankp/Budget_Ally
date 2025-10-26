import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { useState, useEffect } from 'react';

// Register Chart.js components
ChartJS.register(ArcElement, Tooltip, Legend);

export default function SpendingPieChart({ token }) {
  const [categoryData, setCategoryData] = useState(null);
  const [totalSpending, setTotalSpending] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch spending data from backend
    fetch('http://localhost:5000/api/spending-by-category', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    .then(res => res.json())
    .then(data => {
      setCategoryData(data.categories);
      setTotalSpending(data.total_spending);
      setLoading(false);
    })
    .catch(err => {
      console.error('Error fetching spending data:', err);
      setLoading(false);
    });
  }, [token]);

  if (loading) return <div style={{textAlign: 'center', padding: '20px'}}>Loading spending breakdown...</div>;
  if (!categoryData || categoryData.length === 0) {
    return <div style={{textAlign: 'center', padding: '20px'}}>No spending data available yet.</div>;
  }

  // Prepare data for Chart.js
  const chartData = {
    labels: categoryData.map(item => `${item.category} (${item.percentage}%)`),
    datasets: [{
      label: 'Amount ($)',
      data: categoryData.map(item => item.amount),
      backgroundColor: [
        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', 
        '#9966FF', '#FF9F40', '#E7E9ED', '#C9CBCF'
      ],
    }]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    layout: {
      padding: {
        top: 20,
        bottom: 20,
        left: 20,
        right: 20
      }
    },
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          padding: 15,
          font: {
            size: 12
          }
        }
      },
      title: {
        display: true,
        text: `Monthly Spending Breakdown - Total: $${totalSpending.toFixed(2)}`,
        font: {
          size: 16
        },
        padding: {
          bottom: 20
        }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            return `$${context.parsed.toFixed(2)}`;
          }
        }
      }
    }
  };

  return (
    <div style={{ maxWidth: '500px', margin: '20px auto', padding: '20px', border: '1px solid #ddd', borderRadius: '8px' }}>
      <Pie data={chartData} options={options} />
    </div>
  );
}