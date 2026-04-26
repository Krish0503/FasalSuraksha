// Dashboard JS - Animated counters, filtering, search, delete
document.addEventListener('DOMContentLoaded', () => {
  // ===== Animated stat counters =====
  const counters = document.querySelectorAll('.stat-number[data-count]');
  const animateCounter = (el) => {
    const target = parseInt(el.dataset.count, 10) || 0;
    const duration = 1200;
    const startTime = performance.now();
    const update = (now) => {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(target * eased);
      if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
  };

  // Use IntersectionObserver to trigger animation when visible
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(c => observer.observe(c));

  // ===== Animate chart bars =====
  setTimeout(() => {
    document.querySelectorAll('.chart-bar-fill').forEach(bar => {
      const w = bar.dataset.width;
      if (w) bar.style.width = w + '%';
    });
  }, 400);

  // ===== Search / Filter =====
  const searchInput = document.getElementById('historySearch');
  const filterSelect = document.getElementById('historyFilter');
  const grid = document.getElementById('historyGrid');

  function applyFilters() {
    if (!grid) return;
    const query = (searchInput ? searchInput.value.toLowerCase() : '');
    const filter = (filterSelect ? filterSelect.value : 'all');
    const cards = grid.querySelectorAll('.history-card');

    cards.forEach(card => {
      const name = card.dataset.name || '';
      const isHealthy = card.dataset.healthy === 'True';
      let show = true;

      // Search filter
      if (query && !name.includes(query)) show = false;

      // Status filter
      if (filter === 'healthy' && !isHealthy) show = false;
      if (filter === 'diseased' && isHealthy) show = false;

      card.classList.toggle('hidden-card', !show);
    });
  }

  if (searchInput) searchInput.addEventListener('input', applyFilters);
  if (filterSelect) filterSelect.addEventListener('change', applyFilters);

  // ===== Clear all history =====
  const clearBtn = document.getElementById('clearHistoryBtn');
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      showConfirm(
        'Clear All History?',
        'This will permanently delete all your detection history. This cannot be undone.',
        async () => {
          try {
            const res = await fetch('/api/history/clear', { method: 'POST' });
            const data = await res.json();
            if (data.success) {
              window.location.reload();
            } else {
              alert('Failed to clear history.');
            }
          } catch (e) {
            console.error('Clear error:', e);
            alert('An error occurred.');
          }
        }
      );
    });
  }
});

// ===== Delete single detection =====
async function deleteDetection(id, btnEl) {
  showConfirm(
    'Delete Detection?',
    'This entry will be permanently removed from your history.',
    async () => {
      try {
        const res = await fetch(`/api/history/${id}/delete`, { method: 'POST' });
        const data = await res.json();
        if (data.success) {
          const card = btnEl.closest('.history-card');
          if (card) {
            card.style.transition = 'all 0.4s ease';
            card.style.opacity = '0';
            card.style.transform = 'scale(0.8)';
            setTimeout(() => card.remove(), 400);
          }
        } else {
          alert('Failed to delete.');
        }
      } catch (e) {
        console.error('Delete error:', e);
        alert('An error occurred.');
      }
    }
  );
}

// ===== Confirm Modal =====
function showConfirm(title, message, onConfirm) {
  // Remove existing
  const existing = document.querySelector('.dash-confirm-overlay');
  if (existing) existing.remove();

  const overlay = document.createElement('div');
  overlay.className = 'dash-confirm-overlay';
  overlay.innerHTML = `
    <div class="dash-confirm-box">
      <h4>${title}</h4>
      <p>${message}</p>
      <div class="dash-confirm-actions">
        <button class="confirm-cancel">Cancel</button>
        <button class="confirm-delete">Delete</button>
      </div>
    </div>
  `;

  document.body.appendChild(overlay);

  overlay.querySelector('.confirm-cancel').addEventListener('click', () => overlay.remove());
  overlay.addEventListener('click', (e) => { if (e.target === overlay) overlay.remove(); });
  overlay.querySelector('.confirm-delete').addEventListener('click', () => {
    overlay.remove();
    onConfirm();
  });
}
