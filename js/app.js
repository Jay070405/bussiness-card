document.addEventListener('DOMContentLoaded', () => {
    // Dynamic JS Interaction
    document.querySelectorAll('.c-w').forEach(wrap => {
        const container = wrap.querySelector('.c-container');
        const frontContent = wrap.querySelector('.c-f');
        const backContent = wrap.querySelector('.c-b');

        // Click -> Split
        wrap.addEventListener('click', function (e) {
            if (e.target.closest('.btn-h')) return; // Ignore links

            if (this.classList.contains('active')) {
                this.classList.remove('active');
            } else {
                document.querySelectorAll('.c-w.active').forEach(w => w.classList.remove('active'));
                this.classList.add('active');
                // Snap tracking flat for reading
                wrap.style.setProperty('--mx', 0.5);
                wrap.style.setProperty('--my', 0.5);
            }
        });

        // Hover -> 3D Tilt & Material Tracking
        wrap.addEventListener('mousemove', (e) => {
            const rect = wrap.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const xPct = x / rect.width;
            const yPct = y / rect.height;

            const rotateY = (xPct - 0.5) * 45;
            const rotateX = (yPct - 0.5) * -45;

            // Inject coordinates for CSS Gradients (Always run for both states to maintain light source)
            wrap.style.setProperty('--mx', xPct);
            wrap.style.setProperty('--my', yPct);
            frontContent.style.setProperty('--mx', xPct);
            frontContent.style.setProperty('--my', yPct);
            backContent.style.setProperty('--mx', xPct);
            backContent.style.setProperty('--my', yPct);

            // Calculate Angle for Foil Sweeps
            let angle = Math.atan2(yPct - 0.5, xPct - 0.5) * (180 / Math.PI) + 90;
            wrap.style.setProperty('--angle', `${angle}deg`);
            frontContent.style.setProperty('--angle', `${angle}deg`);
            backContent.style.setProperty('--angle', `${angle}deg`);

            if (wrap.classList.contains('active')) {
                // IF ACTIVE (OPEN): Subtly tilt individual cards
                wrap.style.setProperty('--h-rx', `${rotateX * 0.3}deg`);
                wrap.style.setProperty('--h-ry', `${rotateY * 0.3}deg`);
                return;
            }

            // IF CLOSED: Tilt entire container aggressively
            container.classList.remove('reset');
            container.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        // Leave -> Reset
        wrap.addEventListener('mouseleave', () => {
            if (wrap.classList.contains('active')) return;
            container.classList.add('reset');
            wrap.style.setProperty('--mx', 0.5);
            wrap.style.setProperty('--my', 0.5);
            frontContent.style.setProperty('--mx', 0.5);
            frontContent.style.setProperty('--my', 0.5);
            backContent.style.setProperty('--mx', 0.5);
            backContent.style.setProperty('--my', 0.5);
        });
    });
});
