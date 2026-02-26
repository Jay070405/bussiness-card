document.addEventListener('DOMContentLoaded', () => {
    const stageInfo = document.querySelector('h1');
    const ring = document.createElement('div');
    ring.id = 'carousel-ring';

    // Wrap cards in a stage and ring
    const cCont = document.getElementById('c-cont');
    const stage = document.createElement('div');
    stage.id = 'carousel-stage';

    cCont.parentNode.insertBefore(stage, cCont);
    stage.appendChild(ring);

    const cardsArray = Array.from(cCont.querySelectorAll('.scene'));
    cardsArray.forEach(card => ring.appendChild(card));
    cCont.remove(); // Remove old container

    const numCards = cardsArray.length;

    // Math for a perfect cylinder
    // Circumference = numCards * cardWidth
    const cardWidth = 520; // 480px + gap
    const radius = Math.round((cardWidth * numCards) / (2 * Math.PI));
    const anglePerCard = 360 / numCards;

    // Distribute cards in 3D space
    cardsArray.forEach((card, index) => {
        const theta = anglePerCard * index;
        card.style.transform = `rotateY(${theta}deg) translateZ(${radius}px)`;
        // Store the native angle so we can calculate offsets later
        card.dataset.nativeAngle = theta;
    });

    // --- CAROUSEL ROTATION PHYSICS ---
    let currentYRotation = 0;
    let targetYRotation = 0;

    // We add Z translation to pull the camera back or push it in
    let currentZTranslation = -(radius + 800);
    let targetZTranslation = -(radius + 800);

    let isDragging = false;
    let activeCard = null;

    // Wheel Scroll maps directly to rotation
    document.addEventListener('wheel', (e) => {
        if (activeCard) return; // Don't allow scrolling while a card is open inspecting
        // Scroll down (positive delta) -> rotate ring so cards move right -> + angle
        targetYRotation += e.deltaY * 0.15;
    }, { passive: true });

    // Smooth inertia loop
    function animate() {
        // Always lerp both rotation and Z translation
        currentYRotation += (targetYRotation - currentYRotation) * 0.08;
        currentZTranslation += (targetZTranslation - currentZTranslation) * 0.08;

        ring.style.transform = `translateZ(${currentZTranslation}px) rotateY(${currentYRotation}deg)`;

        // Fix 3D CSS hit-testing bugs by completely disabling and hiding the back-half of the cylinder
        cardsArray.forEach((card) => {
            const native = parseFloat(card.dataset.nativeAngle);
            let absAngle = (native + currentYRotation) % 360;
            if (absAngle < 0) absAngle += 360;

            // Cards with an absolute world rotation between 90 and 270 are facing away from the camera
            if (absAngle > 90 && absAngle < 270) {
                card.style.visibility = 'hidden';
                card.style.pointerEvents = 'none';
            } else {
                card.style.visibility = 'visible';
                card.style.pointerEvents = '';
            }
        });

        requestAnimationFrame(animate);
    }
    animate();


    // --- DYNAMIC JS INTERACTION (Hover, Click, Tilt) ---
    document.querySelectorAll('.c-w').forEach((wrap) => {
        const scene = wrap.closest('.scene');
        const container = wrap.querySelector('.c-container');
        const frontContent = wrap.querySelector('.c-f');
        const backContent = wrap.querySelector('.c-b');

        // Click -> Snap to Front & Split
        wrap.addEventListener('click', function (e) {
            if (e.target.closest('.btn-h') || e.target.closest('.social-icon')) return; // Ignore links

            if (this.classList.contains('active')) {
                // CLOSE
                this.classList.remove('active');
                scene.classList.remove('active-spotlight');
                activeCard = null;

                // Pull the ring back to outer view
                targetZTranslation = -(radius + 800);

                // Un-dim all others
                document.querySelectorAll('.scene').forEach(s => s.classList.remove('dimmed'));
            } else {
                // OPEN
                document.querySelectorAll('.c-w.active').forEach(w => w.classList.remove('active'));
                document.querySelectorAll('.scene.active-spotlight').forEach(s => s.classList.remove('active-spotlight'));

                this.classList.add('active');
                scene.classList.remove('dimmed'); // CRITICAL: un-dim the clicked card
                scene.classList.add('active-spotlight');
                activeCard = wrap;

                // Snap tracking flat for reading
                wrap.style.setProperty('--mx', 0.5);
                wrap.style.setProperty('--my', 0.5);

                // Math to snap THIS specific card exactly to 0 degrees facing the camera
                const nativeAngle = parseFloat(scene.dataset.nativeAngle);

                // We want to find the closest multiple of 360 to our current rotation that lands on -nativeAngle
                // Current rotation might be -1440deg. We need to go to -nativeAngle - 1440 if it's closest.
                // A simpler way: just figure out how many full rotations we've done, and lock to that plane.
                let normalizedCurrent = currentYRotation % 360;
                if (normalizedCurrent > 180) normalizedCurrent -= 360;
                if (normalizedCurrent < -180) normalizedCurrent += 360;

                // We want the ring to be rotated at exactly `-nativeAngle`.
                let targetPlane = -nativeAngle;

                // We need to animate there immediately without breaking the lerp loop too harshly.
                // Let's just override targetYRotation to the nearest exact face alignment
                targetYRotation = -nativeAngle;

                // Actually, due to spinning multiple times, we should add/sub 360 until the distance is shortest
                let diff = targetPlane - (currentYRotation % 360);
                if (diff > 180) diff -= 360;
                if (diff < -180) diff += 360;

                targetYRotation = currentYRotation + diff;

                // Zoom the entire ring forward to view the split card closely!
                // Reduced from -300 to -150 to keep the split within the viewport bounds
                targetZTranslation = -(radius - 150);

                // Dim all other cards
                document.querySelectorAll('.scene').forEach(s => {
                    if (s !== scene) s.classList.add('dimmed');
                });
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
