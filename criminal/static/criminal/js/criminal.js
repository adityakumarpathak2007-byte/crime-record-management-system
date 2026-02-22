// Live search filter for criminal list table
const searchInput = document.getElementById('searchInput');
const statusFilter = document.getElementById('statusFilter');
const tableRows = document.querySelectorAll('#criminalTable tbody tr');
const resultsCount = document.getElementById('resultsCount');

function filterTable() {
    const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
    const statusTerm = statusFilter ? statusFilter.value.toLowerCase() : '';
    let visibleCount = 0;

    tableRows.forEach(row => {
        const name = row.querySelector('.col-name') ? row.querySelector('.col-name').textContent.toLowerCase() : '';
        const alias = row.querySelector('.col-alias') ? row.querySelector('.col-alias').textContent.toLowerCase() : '';
        const status = row.querySelector('.col-status') ? row.querySelector('.col-status').textContent.toLowerCase() : '';

        const matchesSearch = name.includes(searchTerm) || alias.includes(searchTerm);
        const matchesStatus = statusTerm === '' || status.includes(statusTerm);

        if (matchesSearch && matchesStatus) {
            row.style.display = '';
            visibleCount++;
        } else {
            row.style.display = 'none';
        }
    });

    if (resultsCount) {
        resultsCount.textContent = `Showing ${visibleCount} record(s)`;
    }
}

if (searchInput) searchInput.addEventListener('input', filterTable);
if (statusFilter) statusFilter.addEventListener('change', filterTable);