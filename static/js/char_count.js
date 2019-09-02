var summaryMaxLength = 500;
var reviewMaxLength = 1500;

$('#summary').keyup(function() {
  var length = $(this).val().length;
  var length = summaryMaxLength-length;
  $('#summary-chars').text(length);
});

$('#review').keyup(function() {
  var length = $(this).val().length;
  var length = reviewMaxLength-length;
  $('#review-chars').text(length);
});