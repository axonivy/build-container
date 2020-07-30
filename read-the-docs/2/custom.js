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

$(document).ready(function() {
  $(".toggle > *").hide();
  $(".toggle .header").show();
  $(".toggle .header").click(function() {
      $(this).parent().children().not(".header").toggle(100);
      $(this).parent().children(".header").toggleClass("open");
  })
});
