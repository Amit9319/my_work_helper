document.getElementById('my-button').addEventListener('click', function() {
    const message = document.getElementById('ticker_id').value;
    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('modal').classList.remove('d-none');
        } else {
            document.getElementById('modal').classList.add('d-none');
            document.getElementById('output').innerHTML = data.table;
            document.getElementById('output_sum').innerText = data.sum;
        }
    });
});

document.getElementById('reset-button').addEventListener('click', function() {
    fetch('/reset')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerHTML = data.table;
            document.getElementById('output_sum').innerText = data.sum;
        });
});

document.querySelectorAll('input[name="options1"]').forEach(option => {
    option.addEventListener('change', function() {
        fetch(`/option/${this.value}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('options1_out').innerText = data.option;
            });
    });
});

document.getElementById('download-button').addEventListener('click', function() {
    html2canvas(document.getElementById('output')).then(canvas => {
        canvas.toBlob(function(blob) {
            const formData = new FormData();
            formData.append('image', blob, 'table.png');
            fetch('/download', {
                method: 'POST',
                body: formData
            })
            .then(response => response.blob())
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = 'table.png';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            });
        });
    });
});
