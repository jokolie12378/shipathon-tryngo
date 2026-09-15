# Tryngo 👕📍

**Try on clothes virtually, then instantly find nearby stores to buy them — fashion meets on-demand transportation.**

Built for SHIPATHON.

---

## Origin

Tryngo started as a SHIPATHON project built around a simple frustration: online "will this look good on me?" tools stop at a picture, and in-store shopping stops at whatever's on the rack in front of you. Neither side talks to the other.

The idea behind Tryngo is to close that gap in one flow:

1. **See it on yourself** — generate a realistic preview of a clothing item on your own photo or avatar before you buy anything.
2. **Decide fast** — like what you see, skip what you don't, without leaving the app.
3. **Get it now** — the moment you like an item, Tryngo checks nearby stores that actually have it in stock and connects that to on-demand transportation, so trying something on virtually can turn into holding it in your hands the same day.

It's fashion discovery and on-demand delivery treated as one problem instead of two separate apps.

## Status

This project is in its early hackathon-scaffold stage. The current repository contains the initial `backend/` and `frontend/` split with no functional pipeline wired up yet — this README documents where the project is headed as much as where it currently stands.

## File Structure

```
shipathon-tryngo/
├── backend/          # Server-side logic (API, data, try-on pipeline orchestration)
├── frontend/         # Client-facing app (UI, avatar viewer, catalog browsing)
├── .gitignore
└── README.md
```

> This structure reflects the top level of the `main` branch as of this writing. If subfolders, additional branches, or specific frameworks have been added since, update this section to match — a `tree -L 3` from a fresh clone is the fastest way to keep this accurate.

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

- **Backend**
  - Handle the user's uploaded photo and kick off 3D avatar generation from it
  - Curate and categorize the clothing dataset (tops, bottoms, shoes, accessories)
  - Call a virtual try-on model/API to generate the 2D preview image
  - Store and serve the catalog + generated previews
  - Handle the swipe-right ("liked this") trigger and hand off to the 3D and store-lookup steps
  - Query nearby store inventory and on-demand transportation APIs once a user commits to an item

- **Frontend**
  - Photo upload flow for creating the user's avatar
  - Catalog browsing UI
  - Display the 2D try-on preview with a swipe left (pass) / swipe right (like) interaction
  - 3D avatar viewer: orbit/rotate + zoom in/out once a garment is applied
  - Store locator + transportation booking hand-off UI

- **3D pipeline** (feeds the frontend's avatar viewer)
  - A small library of base garment template meshes per category (rather than one unique 3D model per catalog item)
  - UV-mapped textures generated from each catalog item's product photo, projected onto the closest-matching template
  - Fitting logic to conform a chosen template to a given user's avatar body
  - Category-matching (e.g. via CLIP embeddings or a cloud vision similarity search) to map an arbitrary real-world garment photo to the right template

## What's Been Done

- [x] Repository scaffolded with `backend/` and `frontend/` split
- [x] Project concept, name, and core user flow defined
- [x] Initial `.gitignore` and base README

## Future Plans

- [ ] Build the photo-upload → 3D avatar creation step (turning a user's selfie/photo into their rigged 3D avatar)
- [ ] Build the 2D virtual try-on step (photo + garment image → generated preview), likely via an existing open-source model (e.g. IDM-VTON, OOTDiffusion, CatVTON) or a paid API (FASHN, fal.ai, Runware)
- [ ] Build a swipe left (pass) / swipe right (like) interaction for browsing try-on previews
- [ ] Curate an initial dataset (target: ~50 tops, 50 bottoms, 50 shoes, 50 accessories) from public fashion datasets (e.g. DressCode, DeepFashion2) plus real product photos
- [ ] Build a small set of base 3D garment templates (~15-20 covering the main silhouettes) rather than modeling every catalog item individually
- [ ] Implement the photo → UV-texture-atlas pipeline so each catalog item's real product photo is projected onto the correct template
- [ ] Implement avatar fitting (Shrinkwrap/skinning) so a template garment conforms to a given user's body proportions
- [ ] Build the 3D viewer with orbit and zoom controls
- [ ] Implement garment category-matching (CLIP embeddings or Google Cloud Vision / Vision Warehouse product search) so an arbitrary real-world photo maps to the right template
- [ ] Integrate nearby store inventory lookup
- [ ] Integrate on-demand transportation booking once a user commits to an item
- [ ] Handle the backend/frontend/3D handoff contract: a clear data format for "user swiped right on item X" → "load template + texture Y onto the avatar"

## Team / Roles

- **Backend**: dataset curation, try-on API orchestration, catalog + preview storage, store/transportation integration
- **Frontend**: catalog UI, preview display, avatar viewer controls
- **3D**: avatar rigging support, garment template library, texture projection, avatar fitting

## License

_Add your chosen license here (e.g. MIT) — none specified yet._