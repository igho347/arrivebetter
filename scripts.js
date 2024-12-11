document.getElementById('calculatorForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = {
        city: document.getElementById('city').value,
        jobType: document.getElementById('jobType').value,
        age: parseInt(document.getElementById('age').value),
        familyStatus: document.getElementById('familyStatus').value
    };

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('result');
        resultElement.innerHTML = `<strong>Success Percentage:</strong> ${data.success_percentage}%`;
        resultElement.style.display = 'block'; // Show the result element
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
