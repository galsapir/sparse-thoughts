(function(document) {
  // Theme toggle
  var themeToggle = document.querySelector('.theme-toggle');
  var html = document.documentElement;

  // Check for saved preference, then system preference
  var savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    html.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    html.setAttribute('data-theme', 'dark');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      var currentTheme = html.getAttribute('data-theme');
      var newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });
  }

  // Listen for system theme changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
      if (!localStorage.getItem('theme')) {
        html.setAttribute('data-theme', e.matches ? 'dark' : 'light');
      }
    });
  }

  // "Show more" on homepage
  var showMoreBtn = document.getElementById('show-more-btn');
  if (showMoreBtn) {
    showMoreBtn.addEventListener('click', function() {
      var hidden = document.querySelectorAll('.post-hidden');
      for (var i = 0; i < hidden.length; i++) {
        hidden[i].classList.remove('post-hidden');
      }
      showMoreBtn.parentElement.remove();
    });
  }

  // Tag filtering on thoughts page
  var tagFilters = document.querySelectorAll('.tag-filter');
  if (tagFilters.length > 0) {
    var items = document.querySelectorAll('.thought-item');
    tagFilters.forEach(function(btn) {
      btn.addEventListener('click', function() {
        var tag = btn.getAttribute('data-tag');

        tagFilters.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');

        items.forEach(function(item) {
          if (tag === 'all' || item.getAttribute('data-tags').split(' ').indexOf(tag) !== -1) {
            item.classList.remove('filtered-out');
          } else {
            item.classList.add('filtered-out');
          }
        });
      });
    });
  }
})(document);
