$(document).ready(function() {
  let categories = [];
  const NUM_CATEGORIES = 6;
  const NUM_CLUES_PER_CAT = 5;
  const apiUrl = 'https://rithm-jeopardy.herokuapp.com/api';

  /** Get NUM_CATEGORIES random category from API.
   *
   * Returns array of category ids
   */
  function getCategoryIds() {
    return $.ajax({
      url: `${apiUrl}/categories?count=${NUM_CATEGORIES}`,
      method: 'GET'
    }).then(response => {
      return response.map(category => category.id);
    });
  }

  /** Return object with data about a category:
   *
   * - id: category ID
   *
   * Returns { title: "Math", clues: clue-array }
   *   where clue-array is {question, answer, showing: null}
   */
  function getCategory(id) {
    return $.ajax({
      url: `${apiUrl}/category?id=${id}`,
      method: 'GET'
    }).then(response => {
      const category = response;
      const clues = category.clues.slice(0, NUM_CLUES_PER_CAT).map(clue => ({
        question: clue.question,
        answer: clue.answer,
        showing: null
      }));
      return { title: category.title, clues };
    });
  }

  /** Setup and start the game */
  async function setupAndStart() {
    $('#game-board').text('Loading...');
    try {
      const categoryIds = await getCategoryIds();
      categories = await Promise.all(categoryIds.map(id => getCategory(id)));
      fillTable();
    } catch (error) {
      console.error("Error setting up and starting the game:", error);
    }
  }

  /** Fill the HTML table with the categories and clues */
  function fillTable() {
    const $board = $('#game-board');
    $board.empty();

    // Create header row with category titles
    const $thead = $('<thead>');
    const $headerRow = $('<tr>');
    for (let category of categories) {
      $headerRow.append($('<th>').text(category.title));
    }
    $thead.append($headerRow);
    $board.append($thead);

    // Create rows for each clue
    const $tbody = $('<tbody>');
    for (let clueIdx = 0; clueIdx < NUM_CLUES_PER_CAT; clueIdx++) {
      const $row = $('<tr>');
      for (let category of categories) {
        $row.append($('<td>').text('?'));
      }
      $tbody.append($row);
    }
    $board.append($tbody);
  }

  setupAndStart();
});