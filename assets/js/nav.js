/* Client-side filter for reference list tables */
(function () {
  var input = document.querySelector("[data-filter-table]");
  if (!input) return;

  var table = document.querySelector(".list-table");
  if (!table) return;

  var rows = Array.prototype.slice.call(table.querySelectorAll("tbody tr"));

  input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase();
    rows.forEach(function (row) {
      var text = row.textContent.toLowerCase();
      row.style.display = !q || text.indexOf(q) !== -1 ? "" : "none";
    });
  });
})();
