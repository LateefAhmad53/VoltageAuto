/* js/script.js */
/* VoltageAuto - Complete Interactive Features */
/* Mobile Menu | Lightbox Gallery | Form Validation | Animations */

document.addEventListener('DOMContentLoaded', () => {
    /* /* ============================================================= */
/* 1. MOBILE MENU TOGGLE */
/* ============================================================= */
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');

// Create overlay dynamically
const overlay = document.createElement('div');
overlay.className = 'overlay';
document.body.appendChild(overlay);

const toggleMobileMenu = () => {
    mobileMenu.classList.toggle('open');
    overlay.classList.toggle('active');
    hamburger.classList.toggle('active');
};

// Click hamburger
hamburger.addEventListener('click', toggleMobileMenu);

// Click overlay to close
overlay.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    overlay.classList.remove('active');
    hamburger.classList.remove('active');
});

    /* ============================================================= */
    /* 2. LIGHTBOX GALLERY SYSTEM (Per-Car, Full Navigation) */
    /* ============================================================= */
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = lightbox.querySelector('.lightbox-img');
    const thumbnailContainer = lightbox.querySelector('.thumbnail-gallery');
    const closeBtn = lightbox.querySelector('.close');
    let currentCarId = null;
    let currentIndex = 0;

    // Gallery images per car (3–5 images)
    const carGalleries = {
        1: ['car1-main.jpg', 'car1-1.jpg', 'car1-2.jpg', 'car1-3.jpg', 'car1-4.jpg', 'car1-5.jpg', 'car1-6.jpg', 'car1-7.jpg', 'car1-8.jpg'],
        2: ['car2-main.jpg', 'car2-1.jpg', 'car2-2.jpg', 'car2-3.jpg', 'car2-4.jpg', 'car2-5.jpg', 'car2-6.jpg', 'car2-7.jpg', 'car2-8.jpg', 'car2-9.jpg', 'car2-10.jpg', 'car2-11.jpg'],
        3: ['car3-main.jpg', 'car3-1.jpg', 'car3-2.jpg', 'car3-3.jpg', 'car3-4.jpg', 'car3-5.jpg',
        'car3-6.jpg', 'car3-7.jpg', 'car3-8.jpg', 'car3-9.jpg',
        ],
        4: ['car4-main.jpg', 'car4-1.jpg', 'car4-2.jpg', 'car4-3.jpg'],
        5: ['car5-main.jpg', 'car5-1.jpg', 'car5-2.jpg', 'car5-3.jpg', 'car5-4.jpg'],
        6: ['car6-main.jpg', 'car6-1.jpg', 'car6-2.jpg', 'car6-3.jpg'],
        7: ['car7-main.jpg', 'car7-1.jpg', 'car7-2.jpg', 'car7-3.jpg', 'car7-4.jpg'],
        8: ['car8-main.jpg', 'car8-1.jpg', 'car8-2.jpg', 'car8-3.jpg', 'car8-4.jpg']
    };

    // Open lightbox
    document.querySelectorAll('.see-more').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const carCard = e.target.closest('.car-card');
            currentCarId = carCard.dataset.car;
            const mainImgSrc = carCard.querySelector('.main-img').src;
            const images = carGalleries[currentCarId];

            currentIndex = images.indexOf(mainImgSrc.split('/').pop());
            if (currentIndex === -1) currentIndex = 0;

            renderGallery(images, currentIndex);
            lightbox.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    });

    // Render main image + thumbnails
    const renderGallery = (images, activeIndex) => {
        lightboxImg.src = `voltage/images/${images[activeIndex]}`;
        lightboxImg.alt = `Car ${currentCarId} - Image ${activeIndex + 1}`;

        thumbnailContainer.innerHTML = '';
        images.forEach((img, idx) => {
            const thumb = document.createElement('img');
            thumb.src = `voltage/images/${img}`;
            thumb.alt = `Car ${currentCarId} - Thumbnail ${idx + 1}`;
            thumb.className = 'gallery-thumb';
            if (idx === activeIndex) thumb.classList.add('active');

            thumb.addEventListener('click', () => {
                currentIndex = idx;
                lightboxImg.src = thumb.src;
                lightboxImg.alt = thumb.alt;
                updateActiveThumb();
            });

            thumbnailContainer.appendChild(thumb);
        });

        updateActiveThumb();
    };

    // Update active thumbnail
    const updateActiveThumb = () => {
        const thumbs = thumbnailContainer.querySelectorAll('.gallery-thumb');
        thumbs.forEach((t, i) => t.classList.toggle('active', i === currentIndex));
    };

    // Close lightbox
    const closeLightbox = () => {
        lightbox.classList.remove('open');
        document.body.style.overflow = '';
        currentCarId = null;
        currentIndex = 0;
    };

    closeBtn.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) closeLightbox();
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('open') || !currentCarId) return;
        const images = carGalleries[currentCarId];
        if (!images) return;

        if (e.key === 'ArrowRight') {
            currentIndex = (currentIndex + 1) % images.length;
        } else if (e.key === 'ArrowLeft') {
            currentIndex = (currentIndex - 1 + images.length) % images.length;
        } else if (e.key === 'Escape') {
            closeLightbox();
            return;
        } else {
            return;
        }
        renderGallery(images, currentIndex);
    });

    // Touch swipe support
    let touchStartX = 0;
    let touchEndX = 0;

    lightbox.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    lightbox.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }, { passive: true });

    const handleSwipe = () => {
        if (!lightbox.classList.contains('open') || !currentCarId) return;
        const images = carGalleries[currentCarId];
        if (!images) return;

        const diff = touchStartX - touchEndX;
        if (Math.abs(diff) > 80) {
            if (diff > 0) {
                currentIndex = (currentIndex + 1) % images.length;
            } else {
                currentIndex = (currentIndex - 1 + images.length) % images.length;
            }
            renderGallery(images, currentIndex);
        }
    };

    /* ============================================================= */
    /* 3. FADE-IN ON SCROLL ANIMATION */
    /* ============================================================= */
    const fadeElements = document.querySelectorAll('.car-card, .service-card, .steps, .benefits, .contact-info, .contact-form');
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    fadeElements.forEach(el => {
        el.classList.add('fade-in');
        fadeObserver.observe(el);
    });

    /* ============================================================= */
    /* 4. CONTACT FORM VALIDATION & SUBMISSION */
    /* ============================================================= */
    const form = document.querySelector('.contact-form');
    if (form) {
        const inputs = {
            name: form.querySelector('#name'),
            email: form.querySelector('#email'),
            phone: form.querySelector('#phone'),
            message: form.querySelector('#message')
        };

        const errorSpans = form.querySelectorAll('.error-msg');
        const successMsg = form.querySelector('.form-success');

        // Real-time validation on blur
        inputs.name.addEventListener('blur', validateName);
        inputs.email.addEventListener('blur', validateEmail);
        inputs.phone.addEventListener('blur', validatePhone);
        inputs.message.addEventListener('blur', validateMessage);

        // Form submission
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            let isValid = true;
            errorSpans.forEach(span => span.textContent = '');
            successMsg.style.display = 'none';

            if (!validateName()) isValid = false;
            if (!validateEmail()) isValid = false;
            if (!validatePhone()) isValid = false;
            if (!validateMessage()) isValid = false;

            if (isValid) {
                successMsg.textContent = `Thank you, ${inputs.name.value.trim()}! Your message has been sent. We'll reply within 24 hours.`;
                successMsg.style.display = 'block';
                form.reset();
                setTimeout(() => successMsg.style.display = 'none', 5000);
            }
        });

        // Validation functions
        function validateName() {
            const value = inputs.name.value.trim();
            const error = inputs.name.parentElement.querySelector('.error-msg');
            if (value === '') {
                error.textContent = 'Name is required';
                return false;
            }
            if (value.length < 2) {
                error.textContent = 'Name must be at least 2 characters';
                return false;
            }
            error.textContent = '';
            return true;
        }

        function validateEmail() {
            const value = inputs.email.value.trim();
            const error = inputs.email.parentElement.querySelector('.error-msg');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (value === '') {
                error.textContent = 'Email is required';
                return false;
            }
            if (!emailRegex.test(value)) {
                error.textContent = 'Please enter a valid email';
                return false;
            }
            error.textContent = '';
            return true;
        }

        function validatePhone() {
            const value = inputs.phone.value.trim();
            const error = inputs.phone.parentElement.querySelector('.error-msg');
            const phoneRegex = /^0[789]\d{9}$/; // Nigerian mobile
            if (value === '') return true; // Optional
            if (!phoneRegex.test(value)) {
                error.textContent = 'Valid Nigerian number (e.g. 08012345678)';
                return false;
            }
            error.textContent = '';
            return true;
        }

        function validateMessage() {
            const value = inputs.message.value.trim();
            const error = inputs.message.parentElement.querySelector('.error-msg');
            if (value === '') {
                error.textContent = 'Message is required';
                return false;
            }
            if (value.length < 10) {
                error.textContent = 'Message must be at least 10 characters';
                return false;
            }
            error.textContent = '';
            return true;
        }
    }

    /* ============================================================= */
    /* 5. SMOOTH SCROLL FOR ANCHOR LINKS */
    /* ============================================================= */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});