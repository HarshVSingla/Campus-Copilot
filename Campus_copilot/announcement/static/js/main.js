document.addEventListener('DOMContentLoaded', function() {
    // Handle announcement card click
    const announcementCards = document.querySelectorAll('.announcement-card:not(.single-view)');
    announcementCards.forEach(card => {
        card.addEventListener('click', function() {
            const url = this.getAttribute('onclick').replace("window.location='", "").replace("'", "");
            window.location.href = url;
        });
    });

    // Add animation class to cards
    const cards = document.querySelectorAll('.announcement-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 50);
        }, index * 100);
    });
});