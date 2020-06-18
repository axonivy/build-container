$(document).ready(function() {
  $(".highlighttable").linkify({
    validate: {
      url: function(value) {
        return /^(http)s?:\/\//.test(value);
      },
      email: function(value) {
        return false;
      }
    }
  });
});
