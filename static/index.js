let btn = document.getElementById('run')

btn.addEventListener('click', () => {
    let x = document.getElementById('code').value
    
    fetch('/run', {
        method: 'post',
        body: x
    }).then(res => {
        return res.text()
    }).then(res => {
        console.log(res)
        let y = document.getElementById('output')
        y.value = res
    })
})