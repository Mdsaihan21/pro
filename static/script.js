function saveEmployee() {

    let name =
    document.getElementById("name").value;

    fetch('/add', {

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            name:name
        })

    })

    .then(response=>response.json())
    .then(data=>{

        alert(data.message);

    });

}

function loadEmployees() {

    fetch('/employees')

    .then(response=>response.json())

    .then(data=>{

        let list =
        document.getElementById("employeeList");

        list.innerHTML = "";

        data.forEach(emp => {

            let li =
            document.createElement("li");

            li.innerText =
            emp[0] + " - " + emp[1];

            list.appendChild(li);

        });

    });

}