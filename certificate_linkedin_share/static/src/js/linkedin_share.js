/** Certificate URL & LinkedIn Share Button
 *  Opens LinkedIn's "Add to Profile" certification flow using the data
 *  attributes rendered server-side on the button (no extra network call
 *  needed — the values are already on the completion page).
 */
(function () {
    "use strict";

    function buildLinkedInUrl(btn) {
        const base = {
            startTask: "CERTIFICATION_NAME",
            name: btn.dataset.certName || "",
            issueYear: btn.dataset.issueYear || "",
            issueMonth: btn.dataset.issueMonth || "",
            certUrl: btn.dataset.certUrl || "",
        };

        // Prefer the official LinkedIn Organization ID when it's configured
        // in Settings (links to the company's real LinkedIn Page). If it's
        // not set, fall back to a plain organization name — never leave
        // both empty/broken, and never send an empty organizationId.
        const orgId = (btn.dataset.orgId || "").trim();
        if (orgId) {
            base.organizationId = orgId;
        } else {
            base.organizationName = btn.dataset.orgName || "";
        }

        const params = new URLSearchParams(base);
        return "https://www.linkedin.com/profile/add?" + params.toString();
    }

    function onClick(ev) {
        const btn = ev.target.closest("#o_certificate_linkedin_btn");
        if (!btn) {
            return;
        }
        ev.preventDefault();
        const url = buildLinkedInUrl(btn);
        window.open(url, "_blank", "noopener,noreferrer");
    }

    // The survey "done" page (where this button lives) is injected into the
    // DOM via an AJAX call after form submission — it does NOT trigger a
    // full page load / DOMContentLoaded. Binding directly to the button on
    // DOMContentLoaded would silently fail because the button doesn't exist
    // yet at that point. Using event delegation on `document` instead means
    // the click is caught no matter when the button was added to the page.
    document.addEventListener("click", onClick);
})();
