# Tryngo 👕📍

**Try on clothes virtually, then instantly find nearby stores to buy them — fashion meets on-demand transportation.**

Built for SHIPATHON.

---

## Origin

Tryngo started as a SHIPATHON project built around a simple frustration: online "will this look good on me?" tools stop at a picture, and in-store shopping stops at whatever's on the rack in front of you. Neither side talks to the other.

The idea behind Tryngo is to close that gap in one flow:

1. **See it on yourself** — generate a realistic preview of a clothing item on your own photo, then see it rendered on your own 3D avatar.
2. **Decide fast** — swipe through items, right to like, left to pass, without leaving the app.
3. **Get it now** — the moment you like an item, Tryngo checks nearby stores that actually have it in stock and connects that to on-demand transportation, so trying something on virtually can turn into holding it in your hands the same day.

It's fashion discovery and on-demand delivery treated as one problem instead of two separate apps.

## Status

Work is currently split across branches, each further along than `main`:

- **`3d-vis`** — a working 3D avatar viewer (Vite + React) with a base avatar model and three outfit templates already built as `.glb` assets.
- **backend branch** — a real FastAPI service with routing, database models, request/response schemas, and an initial data-seeding script.

This README merges both into one picture of where the project actually stands, and what's left to connect the pieces into a single working app.

## File Structure

```
shipathon-tryngo/
├── 3d/
│   └── viewer/                     # 3D avatar viewer app (Vite + React) — from `3d-vis`
│       ├── public/
│       │   ├── models/
│       │   │   ├── avatar.glb              # base user avatar model
│       │   │   ├── business_casual.glb     # outfit template
│       │   │   ├── chill_outfit.glb        # outfit template
│       │   │   └── military_outfit.glb     # outfit template
│       │   ├── favicon.svg
│       │   └── icons.svg
│       ├── src/
│       │   ├── assets/
│       │   │   ├── hero.png
│       │   │   ├── react.svg
│       │   │   └── vite.svg
│       │   ├── App.jsx
│       │   ├── App.css
│       │   ├── index.css
│       │   └── main.jsx
│       ├── index.html
│       ├── package.json
│       ├── package-lock.json
│       ├── vite.config.js
│       ├── eslint.config.js
│       └── README.md
├── backend/                         # FastAPI service — from backend branch
│   ├── .gitignore
│   ├── .vscode/
│   │   └── settings.json
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI app entry point
│   │   ├── database.py              # DB connection/session setup
│   │   ├── models.py                # ORM models
│   │   ├── schemas.py               # Pydantic request/response schemas
│   │   ├── seed_data.py             # Seeds the DB with initial catalog data
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── clothing.py          # Clothing catalog endpoints
│   │   └── services/
│   │       └── __init__.py
│   └── requirements.txt
├── frontend/
│   ├── package.json
│   └── src/
│       └── package.json
├── .gitignore
└── README.md
```

> **Notes on reconciling branches:**
> - The `3d-vis` branch's own `backend/` folder is a bare Node-style scaffold (just a `package.json`) — the real backend work lives on the backend branch shown above (FastAPI). Treat the FastAPI version as the source of truth and drop the Node stub once branches are merged.
> - `frontend/` currently has a `package.json` at its root *and* another inside `src/` on both branches — consistent enough that it may be intentional, but worth a quick sanity check before more is built on top of it.
> - No changes have been merged into `main` yet — `main` is still the original bare scaffold.

## How It's Meant to Work (Target Pipeline)

```
User uploads a photo of themselves
        │
        ▼
3D avatar created from that photo
        │
        ▼
Browse catalog (tops / bottoms / shoes / accessories)
        │
        ▼
2D virtual try-on preview generated (user photo + garment image → composite image)
        │
        ▼
User swipes on the preview
   │                    │
Swipe left (pass)   Swipe right (like)
   │                    │
Back to browse       Fit the garment onto the user's 3D avatar (rotate/zoom viewer)
                            │
                            ▼
                    Check nearby store inventory for that item
                            │
                            ▼
                    Connect to on-demand transportation to go get it
```

### Component breakdown

- **Backend** (FastAPI — `backend/app/`)
  - Handle the user's uploaded photo and kick off 3D avatar generation from it
  - Curate and categorize the clothing dataset (tops, bottoms, shoes, accessories) — `seed_data.py` is the starting point
  - Serve the catalog through `routers/clothing.py`
  - Call a virtual try-on model/API to generate the 2D preview image
  - Handle the swipe-right ("liked this") trigger and hand off to the 3D and store-lookup steps
  - Query nearby store inventory and on-demand transportation APIs once a user commits to an item

- **Frontend**
  - Photo upload flow for creating the user's avatar
  - Catalog browsing UI
  - Display the 2D try-on preview with a swipe left (pass) / swipe right (like) interaction
  - Store locator + transportation booking hand-off UI

- **3D viewer** (`3d/viewer/` — Vite + React)
  - Renders the user's avatar (`avatar.glb`) and applies outfit templates on top of it
  - Orbit/rotate + zoom in/out controls
  - Currently ships with three bundled outfit templates; needs to load templates dynamically based on what the user picks, instead of a fixed set
  - A growing library of base garment template meshes per category (rather than one unique 3D model per catalog item)
  - UV-mapped textures generated from each catalog item's product photo, projected onto the closest-matching template
  - Fitting logic to conform a chosen template to a given user's avatar body
  - Category-matching (e.g. via CLIP embeddings or a cloud vision similarity search) to map an arbitrary real-world garment photo to the right template

## What's Been Done

- [x] Repository scaffolded with `backend/` and `frontend/` split
- [x] Project concept, name, and core user flow defined
- [x] 3D avatar viewer scaffolded as its own Vite + React app (`3d/viewer/`)
- [x] Base avatar model created (`avatar.glb`)
- [x] First three outfit templates built (`business_casual.glb`, `chill_outfit.glb`, `military_outfit.glb`) — the start of the garment template library
- [x] Backend rebuilt as a real FastAPI service: app entry point, database setup, ORM models, Pydantic schemas
- [x] Clothing catalog router (`routers/clothing.py`) started
- [x] Initial data-seeding script (`seed_data.py`) in place for populating the catalog

## Future Plans

- [ ] Merge `3d-vis` and the backend branch into `main`, dropping the unused Node `backend/package.json` stub
- [ ] Build the photo-upload → 3D avatar creation step (turning a user's selfie/photo into an `avatar.glb`-style rigged model)
- [ ] Build the 2D virtual try-on step (photo + garment image → generated preview), likely via an existing open-source model (e.g. IDM-VTON, OOTDiffusion, CatVTON) or a paid API (FASHN, fal.ai, Runware)
- [ ] Build the swipe left (pass) / swipe right (like) interaction for browsing try-on previews
- [ ] Curate the full dataset (target: ~50 tops, 50 bottoms, 50 shoes, 50 accessories) and expand `seed_data.py` to populate it — from public fashion datasets (e.g. DressCode, DeepFashion2) plus real product photos
- [ ] Flesh out the clothing router beyond its current starting point (filtering by category, fetching by ID, etc.)
- [ ] Expand the outfit template library beyond the current three to cover the full tops/bottoms/shoes/accessories split
- [ ] Implement the photo → UV-texture-atlas pipeline so each catalog item's real product photo is projected onto the correct template
- [ ] Implement avatar fitting (Shrinkwrap/skinning) so a template garment conforms to a given user's body proportions
- [ ] Wire up dynamic template loading + outfit-swapping in `3d/viewer`, replacing the current fixed set of three bundled `.glb` files
- [ ] Implement garment category-matching (CLIP embeddings or Google Cloud Vision / Vision Warehouse product search) so an arbitrary real-world photo maps to the right template
- [ ] Integrate nearby store inventory lookup
- [ ] Integrate on-demand transportation booking once a user commits to an item
- [ ] Define the backend/frontend/3D handoff contract: a clear data format for "user swiped right on item X" → "load template + texture Y onto the avatar"

## Team / Roles

- **Backend**: dataset curation, catalog API, try-on API orchestration, store/transportation integration
- **Frontend**: catalog UI, photo upload, preview display, swipe interaction
- **3D**: avatar viewer, garment template library, texture projection, avatar fitting