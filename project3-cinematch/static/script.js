javascript

const genreCheckboxes = document.querySelectorAll(
    'input[name="genres"]'
);

const selectionCount = document.getElementById(
    "selectionCount"
);

function updateSelectionCount() {
    const selected = document.querySelectorAll(
        'input[name="genres"]:checked'
    ).length;

    selectionCount.textContent =
        `${selected} selected`;
}

genreCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener(
        "change",
        updateSelectionCount
    );
});

updateSelectionCount();