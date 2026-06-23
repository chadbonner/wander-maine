-- Wander Maine: locations table
-- Run this migration to set up the database schema.

create table if not exists public.locations (
  id          bigint generated always as identity primary key,
  name        text not null,
  category    text not null check (category in ('Outdoors', 'Food & Dining', 'Culture')),
  region      text,
  town        text,
  description text,
  price       text,
  season      text,
  maps_url    text,
  lat         double precision,
  lng         double precision,
  created_at  timestamptz default now()
);

create index if not exists locations_region_idx   on public.locations (region);
create index if not exists locations_category_idx on public.locations (category);

-- Enable Row Level Security
alter table public.locations enable row level security;

-- Public read-only policy (no authentication required to view locations)
create policy "Public read access"
  on public.locations
  for select
  to anon, authenticated
  using (true);
