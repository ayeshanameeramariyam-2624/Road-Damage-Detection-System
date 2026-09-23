const table = document.getElementById("damageTable");

const totalDamage = document.getElementById("totalDamage");
const potholes = document.getElementById("potholes");
const highPriority = document.getElementById("highPriority");
const totalCost = document.getElementById("totalCost");

fetch("http://127.0.0.1:5000/damage")
    .then(response => response.json())
    .then(data => {

        totalDamage.textContent = data.length;

        let potholeCount = 0;
        let highCount = 0;
        let cost = 0;

        table.innerHTML = "";

        data.forEach(item => {

            if (item.damage_type.toLowerCase() === "pothole") {
                potholeCount++;
            }

            if (item.priority.toLowerCase() === "high") {
                highCount++;
            }

            cost += Number(item.estimated_cost);

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${item.id}</td>
                <td>${item.damage_type}</td>
                <td>${item.severity}</td>
                <td>${item.latitude}</td>
                <td>${item.longitude}</td>
                <td>${item.priority}</td>
                <td>₹${item.estimated_cost}</td>
            `;

            table.appendChild(row);
        });

        potholes.textContent = potholeCount;
        highPriority.textContent = highCount;
        totalCost.textContent = "₹" + cost;
    })
    .catch(error => {
        console.error(error);
        table.innerHTML = `
            <tr>
                <td colspan="7">Backend data not available</td>
            </tr>
        `;
    });
