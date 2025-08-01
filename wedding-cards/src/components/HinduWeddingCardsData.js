

import blueWeddingCard from "../assets/images/beach-card.png";
import ganeshaWeddingCard from "../assets/images/ganesha.png";
import favourBoxWeddingCard from "../assets/images/favour-box.png";
import themeWeddingCard from "../assets/images/theme.png";
import vintageWeddingCard from "../assets/images/vintage.png";
import peacockWeddingCard from "../assets/images/peacock.png";
import uniqueWeddingCard from "../assets/images/unique.jpg";
import wardrobeWeddingCard from "../assets/images/wardrobe.png";
import editableWeddingCard from "../assets/images/foldable.jpg";
import traditionalWeddingCard from "../assets/images/traditional2.png";
import scrollWeddingCard from "../assets/images/scroll.png";
import gatefoldWeddingCard from "../assets/images/gatefold.png";

// Example variant (you can change image paths accordingly)
import lavenderVariant from "../assets/images/card1.jpg";

export const cards = [
  {
    id: 1,
    title: "The Blue Wedding Cards",
    price: 72.25,
    sku: "KSN0054",
    src: blueWeddingCard,
    gallery: [blueWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard, lavenderVariant],
    description:
      "The blue wedding card has embossed floral design with customized initial acrylic nameplate.\nThis invitation card has holding insert and an envelope",
    comments: "Discounts are applied based on quantity at checkout",
    height: "27.5",
    width: "21",
    weight: "110",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 2,
    title: "Ganesha Wedding Cards",
    price: 25.25,
    sku: "KSN0055",
    src: ganeshaWeddingCard,
    gallery: [ganeshaWeddingCard, gatefoldWeddingCard, favourBoxWeddingCard, themeWeddingCard],
    
    description: "Elegant card with Ganesha motif and traditional layout.",
    comments: "Available in 3 colors.",
    height: "24",
    width: "18",
    weight: "90",
     variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 3,
    title: "Wedding Cards Favour Box",
    price: 39.45,
    sku: "KSN0056",
    src: favourBoxWeddingCard,
    gallery: [favourBoxWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Favor box style card with space for gifts.",
    comments: "Customizable with name/date.",
    height: "22",
    width: "19",
    weight: "100",
     variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 4,
    title: "Theme Wedding Cards",
    price: 30.0,
    sku: "KSN0057",
    src: themeWeddingCard,
    gallery: [themeWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Theme-based design matching your event color palette.",
    comments: "Match with invitation set.",
    height: "26",
    width: "20",
    weight: "105",
     variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 5,
    title: "Vintage Wedding Cards",
    price: 30.15,
    sku: "KSN0058",
    src: vintageWeddingCard,
    gallery: [vintageWeddingCard, gatefoldWeddingCard, favourBoxWeddingCard,themeWeddingCard],
    description: "Vintage theme with rustic textures and warm tones.",
    comments: "Great for outdoor weddings.",
    height: "25.5",
    width: "20",
    weight: "102",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 6,
    title: "Elegant Peacock Wedding Cards",
    price: 15.0,
    sku: "KSN0059",
    src: peacockWeddingCard,
    gallery: [peacockWeddingCard, gatefoldWeddingCard, favourBoxWeddingCard,themeWeddingCard],
    description: "Peacock feather elements with a royal feel.",
    comments: "Foil stamping available.",
    height: "24",
    width: "18",
    weight: "95",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 7,
    title: "Unique Wedding Cards",
    price: 22.5,
    sku: "KSN0060",
    src: uniqueWeddingCard,
    gallery: [uniqueWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Modern layout with unique pop-up design.",
    comments: "Stand-out design for modern couples.",
    height: "28",
    width: "22",
    weight: "120",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 8,
    title: "Wardrobe Wedding Cards",
    price: 59.75,
    sku: "KSN0061",
    src: wardrobeWeddingCard,
    gallery: [wardrobeWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Mini-wardrobe box style invitation with drawers.",
    comments: "Luxury category invitation.",
    height: "30",
    width: "25",
    weight: "150",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 9,
    title: "Editable Wedding Cards",
    price: 35.55,
    sku: "KSN0062",
    src: editableWeddingCard,
    gallery: [editableWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Editable templates that you can customize online.",
    comments: "Download & print yourself.",
    height: "21",
    width: "15",
    weight: "N/A (digital)",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 10,
    title: "Traditional Wedding Cards",
    price: 25.0,
    sku: "KSN0063",
    src: traditionalWeddingCard,
    gallery: [traditionalWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Classic traditional style with Sanskrit text options.",
    comments: "Popular in Tamil, Telugu & Kannada weddings.",
    height: "26",
    width: "20",
    weight: "100",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 11,
    title: "Royal Scroll Wedding Cards",
    price: 75.0,
    sku: "KSN0064",
    src: scrollWeddingCard,
    gallery: [scrollWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Royal scroll-style invitation with velvet pouch.",
    comments: "Best seller in luxury weddings.",
    height: "32",
    width: "24",
    weight: "180",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
  {
    id: 12,
    title: "Gate Folding Wedding Cards",
    price: 43.2,
    sku: "KSN0065",
    src: gatefoldWeddingCard,
    gallery: [gatefoldWeddingCard, gatefoldWeddingCard, ganeshaWeddingCard,themeWeddingCard],
    description: "Gate-folding cards with floral motifs.",
    comments: "Available in multiple floral themes.",
    height: "27",
    width: "21",
    weight: "110",
    variants: [
      {
        id: 101,
        title: "Lavender Variant",
        src: lavenderVariant,
      },
    ],
  },
];