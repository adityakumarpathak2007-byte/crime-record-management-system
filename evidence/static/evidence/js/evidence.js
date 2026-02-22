const searchInput = document.getElementById('searchInput');
const typeFilter = document.getElementById('typeFilter');
const tableRows = document.querySelectorAll('#evidenceTable tbody tr');
const resultsCount = document.getElementById('resultsCount');

function filterTable() {
    const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
    const typeTerm = typeFilter ? typeFilter.value.toLowerCase() : '';
    let visibleCount = 0;

    tableRows.forEach(row => {
        const text = row.textContent.toLowerCase();
        const type = row.querySelector('.col-type') ? row.querySelector('.col-type').textContent.toLowerCase() : '';
        const matchesSearch = text.includes(searchTerm);
        const matchesType = typeTerm === '' || type.includes(typeTerm);

        if (matchesSearch && matchesType) {
            row.style.display = '';
            visibleCount++;
        } else {
            row.style.display = 'none';
        }
    });

    if (resultsCount) resultsCount.textContent = `Showing ${visibleCount} record(s)`;
}

if (searchInput) searchInput.addEventListener('input', filterTable);
if (typeFilter) typeFilter.addEventListener('change', filterTable);