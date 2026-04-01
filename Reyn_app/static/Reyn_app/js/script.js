/* ================================================
       NAVIGATION — scroll state & active section
       ================================================ */
    const navbar   = document.getElementById('navbar');
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a, .mobile-menu a');

    window.addEventListener('scroll', () => {
      /* Add shadow on scroll */
      navbar.classList.toggle('scrolled', window.scrollY > 20);

      /* Active nav link based on scroll position */
      let current = '';
      sections.forEach(sec => {
        const top = sec.offsetTop - 90;
        if (window.scrollY >= top) current = sec.id;
      });
      navLinks.forEach(a => {
        a.classList.toggle('active', a.getAttribute('href') === `#${current}`);
      });

      /* Back to top visibility */
      document.getElementById('back-to-top').classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });

    /* Back to top click */
    document.getElementById('back-to-top').addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    /* ================================================
       HAMBURGER MOBILE MENU
       ================================================ */
    const hamburger  = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');

    hamburger.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.toggle('open');
      hamburger.classList.toggle('open', isOpen);
      hamburger.setAttribute('aria-expanded', String(isOpen));
    });

    /* Close mobile menu when a link is clicked */
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });

    /* ================================================
       SCROLL REVEAL — IntersectionObserver
       ================================================ */
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');

          /* Trigger skill bar fills when skill section enters view */
          if (entry.target.classList.contains('skill-bars') || entry.target.closest('.skill-bars')) {
            animateSkillBars();
          }
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    /* ================================================
       SKILL BAR ANIMATION
       ================================================ */
    function animateSkillBars() {
      document.querySelectorAll('.skill-bar-fill').forEach(bar => {
        const pct = bar.getAttribute('data-pct');
        setTimeout(() => { bar.style.width = pct + '%'; }, 200);
      });
    }

    /* Also trigger bars when parent section is observed */
    const skillBarsEl = document.querySelector('.skill-bars');
    if (skillBarsEl) {
      const barsObserver = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting) {
          animateSkillBars();
          barsObserver.disconnect();
        }
      }, { threshold: 0.3 });
      barsObserver.observe(skillBarsEl);
    }

    /* ================================================
       PROJECT FILTER TABS
       ================================================ */
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        /* Update active state */
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');

        projectCards.forEach(card => {
          const cat = card.getAttribute('data-category');
          const match = filter === 'all' || cat === filter;

          /* Fade + hide with CSS transition */
          if (match) {
            card.style.display = '';
            requestAnimationFrame(() => {
              card.style.opacity = '1';
              card.style.transform = '';
            });
          } else {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.95)';
            setTimeout(() => {
              if (btn.getAttribute('data-filter') !== 'all' &&
                  card.getAttribute('data-category') !== btn.getAttribute('data-filter')) {
                card.style.display = 'none';
              }
            }, 300);
          }
        });
      });
    });

    /* ================================================
       LIGHTBOX
       ================================================ */
    function openLightbox(src, caption) {
      const lb    = document.getElementById('lightbox');
      const img   = document.getElementById('lightbox-img');
      const cap   = document.getElementById('lightbox-cap');
      img.src     = src;
      cap.textContent = caption;
      lb.style.display = 'flex';
      /* Trigger opacity transition after display */
      requestAnimationFrame(() => lb.classList.add('open'));
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox(e) {
      if (e && e.target !== document.getElementById('lightbox') &&
          !e.target.classList.contains('lightbox-close') &&
          !e.target.closest('.lightbox-close')) return;
      const lb = document.getElementById('lightbox');
      lb.classList.remove('open');
      document.body.style.overflow = '';
      setTimeout(() => { lb.style.display = 'none'; }, 300);
    }

    /* Keyboard close */
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeLightbox({ target: document.getElementById('lightbox') });
    });

    /* ================================================
       CONTACT FORM — Simulated submit
       ================================================ */
    function handleFormSubmit() {
      const name    = document.getElementById('name').value.trim();
      const email   = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      if (!name || !email || !message) {
        showToast('✍️ Please fill out all required fields!');
        return;
      }

      /* Simulate success */
      showToast('✉️ Message sent! I\'ll reply soon 🌸');
      document.getElementById('name').value    = '';
      document.getElementById('email').value   = '';
      document.getElementById('subject').value = '';
      document.getElementById('message').value = '';
    }

    /* ================================================
       TOAST NOTIFICATION
       ================================================ */
    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3500);
    }

    /* ================================================
       SMOOTH SCROLL for anchor links
       ================================================ */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });