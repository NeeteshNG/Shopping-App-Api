import os
import urllib.request
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from products.models import Product, ProductImage
import random

class Command(BaseCommand):
    help = 'Seed database with sample products and images'

    CATEGORIES = [
        'Electronics',
        'Clothing',
        'Home & Kitchen',
        'Sports & Outdoors',
        'Books',
        'Beauty & Personal Care',
        'Toys & Games',
        'Automotive',
        'Health & Wellness',
        'Jewelry & Watches'
    ]

    PRODUCTS_DATA = {
        'Electronics': [
            ('Wireless Bluetooth Headphones', 'Premium over-ear headphones with active noise cancellation, 30-hour battery life, and superior sound quality.', 79.99, 149.99),
            ('Smart Watch Pro', 'Feature-rich smartwatch with heart rate monitor, GPS, and 7-day battery life.', 199.99, 299.99),
            ('Portable Bluetooth Speaker', 'Waterproof speaker with 360-degree sound and 12-hour playtime.', 49.99, 79.99),
            ('Wireless Earbuds', 'True wireless earbuds with touch controls and charging case.', 39.99, 69.99),
            ('USB-C Hub Adapter', '7-in-1 hub with HDMI, USB 3.0, and SD card reader.', 29.99, 49.99),
            ('Mechanical Gaming Keyboard', 'RGB backlit keyboard with blue switches and programmable keys.', 89.99, 129.99),
            ('Wireless Gaming Mouse', 'High-precision mouse with 16000 DPI and customizable buttons.', 59.99, 89.99),
            ('4K Webcam', 'Ultra HD webcam with auto-focus and built-in microphone.', 79.99, 119.99),
            ('Portable Power Bank 20000mAh', 'Fast charging power bank with dual USB ports.', 34.99, 54.99),
            ('Smart Home Hub', 'Central hub for controlling all your smart devices.', 99.99, 149.99),
        ],
        'Clothing': [
            ('Classic Cotton T-Shirt', 'Comfortable 100% cotton t-shirt available in multiple colors.', 19.99, 29.99),
            ('Slim Fit Jeans', 'Modern slim fit denim jeans with stretch comfort.', 49.99, 79.99),
            ('Casual Hoodie', 'Soft fleece hoodie with kangaroo pocket.', 39.99, 59.99),
            ('Formal Dress Shirt', 'Wrinkle-resistant dress shirt for professional settings.', 34.99, 54.99),
            ('Athletic Shorts', 'Breathable shorts with moisture-wicking technology.', 24.99, 39.99),
            ('Winter Jacket', 'Insulated jacket with waterproof exterior.', 89.99, 149.99),
            ('Leather Belt', 'Genuine leather belt with classic buckle.', 29.99, 49.99),
            ('Running Shoes', 'Lightweight shoes with cushioned sole.', 79.99, 129.99),
            ('Wool Sweater', 'Soft merino wool sweater for cold weather.', 59.99, 89.99),
            ('Casual Sneakers', 'Versatile sneakers for everyday wear.', 54.99, 84.99),
        ],
        'Home & Kitchen': [
            ('Stainless Steel Cookware Set', '10-piece cookware set with non-stick coating.', 129.99, 199.99),
            ('Air Fryer XL', 'Large capacity air fryer with digital controls.', 89.99, 139.99),
            ('Coffee Maker with Grinder', 'Programmable coffee maker with built-in grinder.', 79.99, 119.99),
            ('Knife Set with Block', '15-piece professional knife set.', 69.99, 109.99),
            ('Instant Pot Multi-Cooker', '7-in-1 electric pressure cooker.', 79.99, 129.99),
            ('Blender Pro', 'High-powered blender for smoothies and soups.', 59.99, 99.99),
            ('Toaster Oven', 'Convection toaster oven with multiple functions.', 49.99, 79.99),
            ('Electric Kettle', 'Fast-boiling kettle with temperature control.', 34.99, 54.99),
            ('Food Storage Container Set', '24-piece airtight container set.', 29.99, 49.99),
            ('Stand Mixer', 'Professional stand mixer with multiple attachments.', 199.99, 299.99),
        ],
        'Sports & Outdoors': [
            ('Yoga Mat Premium', 'Extra thick non-slip yoga mat.', 29.99, 49.99),
            ('Dumbbell Set', 'Adjustable dumbbell set 5-25 lbs.', 149.99, 249.99),
            ('Camping Tent 4-Person', 'Waterproof tent with easy setup.', 89.99, 149.99),
            ('Hiking Backpack 40L', 'Durable backpack with hydration compatible.', 59.99, 99.99),
            ('Resistance Bands Set', '5-piece resistance bands with handles.', 24.99, 39.99),
            ('Bicycle Helmet', 'Lightweight helmet with adjustable fit.', 39.99, 69.99),
            ('Fitness Tracker', 'Track steps, calories, and sleep patterns.', 49.99, 79.99),
            ('Jump Rope Speed', 'Adjustable speed rope for cardio workouts.', 14.99, 24.99),
            ('Foam Roller', 'High-density foam roller for muscle recovery.', 24.99, 39.99),
            ('Water Bottle Insulated', 'Double-wall insulated bottle keeps drinks cold 24hrs.', 19.99, 34.99),
        ],
        'Books': [
            ('The Art of Programming', 'Comprehensive guide to software development.', 39.99, 59.99),
            ('Mindfulness for Beginners', 'Introduction to meditation and mindful living.', 14.99, 24.99),
            ('World History Encyclopedia', 'Illustrated guide to world history.', 29.99, 49.99),
            ('Cooking Masterclass', 'Learn techniques from professional chefs.', 24.99, 39.99),
            ('Financial Freedom Guide', 'Practical steps to financial independence.', 19.99, 29.99),
            ('Science Fiction Collection', 'Anthology of classic sci-fi stories.', 16.99, 26.99),
            ('Photography Essentials', 'Master the art of photography.', 34.99, 54.99),
            ('Language Learning Made Easy', 'Quick methods to learn new languages.', 22.99, 34.99),
            ('Gardening for All Seasons', 'Year-round gardening tips and tricks.', 18.99, 28.99),
            ('Business Strategy Handbook', 'Proven strategies for business success.', 27.99, 44.99),
        ],
        'Beauty & Personal Care': [
            ('Skincare Set Complete', 'Cleanser, toner, and moisturizer combo.', 49.99, 79.99),
            ('Hair Dryer Professional', 'Ionic hair dryer with multiple heat settings.', 59.99, 99.99),
            ('Electric Toothbrush', 'Sonic toothbrush with multiple modes.', 39.99, 69.99),
            ('Perfume Gift Set', 'Collection of premium fragrances.', 79.99, 129.99),
            ('Makeup Brush Set', '12-piece professional brush set.', 29.99, 49.99),
            ('Face Mask Variety Pack', 'Sheet masks for different skin types.', 19.99, 34.99),
            ('Hair Straightener', 'Ceramic flat iron with adjustable temperature.', 44.99, 74.99),
            ('Nail Care Kit', 'Complete manicure and pedicure set.', 24.99, 39.99),
            ('Body Lotion Set', 'Moisturizing lotions in various scents.', 34.99, 54.99),
            ('Beard Grooming Kit', 'Oil, balm, and brush for beard care.', 29.99, 49.99),
        ],
        'Toys & Games': [
            ('Building Blocks 1000pc', 'Creative building set compatible with major brands.', 29.99, 49.99),
            ('Remote Control Car', 'High-speed RC car with rechargeable battery.', 39.99, 69.99),
            ('Board Game Collection', 'Classic family board games bundle.', 34.99, 54.99),
            ('Puzzle 1000 Pieces', 'Challenging jigsaw puzzle with beautiful artwork.', 14.99, 24.99),
            ('Action Figure Set', 'Collectible figures with accessories.', 24.99, 44.99),
            ('Drone with Camera', 'Beginner-friendly drone with HD camera.', 79.99, 129.99),
            ('Educational Tablet for Kids', 'Learning tablet with games and activities.', 69.99, 109.99),
            ('Stuffed Animal Giant', 'Extra large plush toy for cuddling.', 29.99, 49.99),
            ('Card Game Bundle', 'Popular card games collection.', 19.99, 34.99),
            ('Science Kit Chemistry', 'Safe chemistry experiments for kids.', 34.99, 54.99),
        ],
        'Automotive': [
            ('Car Phone Mount', 'Universal mount with wireless charging.', 24.99, 39.99),
            ('Dash Camera HD', 'Front and rear recording dash cam.', 79.99, 129.99),
            ('Car Vacuum Cleaner', 'Portable handheld vacuum for cars.', 34.99, 54.99),
            ('Tire Inflator Portable', 'Digital tire pump with auto shutoff.', 39.99, 59.99),
            ('Car Seat Covers Set', 'Universal fit seat covers.', 49.99, 79.99),
            ('Jump Starter Power Pack', 'Emergency jump starter with USB ports.', 69.99, 109.99),
            ('Car Cleaning Kit', 'Complete interior and exterior cleaning set.', 29.99, 49.99),
            ('LED Headlight Bulbs', 'Bright LED replacement bulbs pair.', 44.99, 74.99),
            ('Steering Wheel Cover', 'Premium leather steering wheel cover.', 19.99, 34.99),
            ('Trunk Organizer', 'Collapsible organizer with multiple compartments.', 24.99, 39.99),
        ],
        'Health & Wellness': [
            ('Blood Pressure Monitor', 'Digital arm blood pressure monitor.', 39.99, 69.99),
            ('Massage Gun', 'Percussion massager for muscle relief.', 89.99, 149.99),
            ('Digital Scale Smart', 'Body composition scale with app.', 34.99, 54.99),
            ('Pill Organizer Weekly', 'Large compartment pill dispenser.', 9.99, 16.99),
            ('Thermometer Digital', 'Instant-read forehead thermometer.', 24.99, 39.99),
            ('Humidifier Ultrasonic', 'Quiet humidifier for bedroom.', 44.99, 74.99),
            ('First Aid Kit Complete', '200-piece emergency first aid kit.', 29.99, 49.99),
            ('Aromatherapy Diffuser', 'Essential oil diffuser with LED lights.', 29.99, 49.99),
            ('Heating Pad Electric', 'Extra large heating pad with auto shutoff.', 34.99, 54.99),
            ('Posture Corrector', 'Adjustable back support brace.', 19.99, 34.99),
        ],
        'Jewelry & Watches': [
            ('Silver Necklace Chain', 'Sterling silver chain necklace.', 39.99, 69.99),
            ('Analog Watch Classic', 'Leather band analog watch.', 79.99, 129.99),
            ('Earrings Set Gold', 'Pack of 6 gold-plated earrings.', 24.99, 44.99),
            ('Bracelet Charm', 'Adjustable charm bracelet.', 29.99, 49.99),
            ('Ring Set Stackable', '5-piece stackable ring set.', 19.99, 34.99),
            ('Watch Digital Sport', 'Water-resistant digital sports watch.', 49.99, 79.99),
            ('Pendant Heart', 'Heart-shaped pendant with chain.', 34.99, 59.99),
            ('Cufflinks Set', 'Elegant cufflinks for formal wear.', 29.99, 49.99),
            ('Anklet Gold Plated', 'Delicate gold-plated anklet.', 14.99, 24.99),
            ('Watch Box Organizer', 'Leather watch storage box.', 39.99, 64.99),
        ],
    }

    # Placeholder image URLs (using picsum.photos for random images)
    def get_image_url(self, category, index):
        # Use consistent seed for reproducible images
        seed = hash(f"{category}_{index}") % 1000
        return f"https://picsum.photos/seed/{seed}/800/800"

    def download_image(self, url, filename):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                return ContentFile(response.read(), name=filename)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Failed to download image: {e}'))
            return None

    def handle(self, *args, **options):
        self.stdout.write('Starting database seed...')

        # Check if products already exist
        if Product.objects.count() > 0:
            self.stdout.write(self.style.WARNING('Products already exist. Skipping seed.'))
            self.stdout.write(self.style.SUCCESS(f'Current product count: {Product.objects.count()}'))
            return

        product_count = 0
        image_count = 0

        for category, products in self.PRODUCTS_DATA.items():
            self.stdout.write(f'Creating products for category: {category}')

            for idx, (name, description, price, original_price) in enumerate(products):
                # Create product
                product = Product.objects.create(
                    name=name,
                    description=description,
                    price=price,
                    category=category,
                    stock=random.randint(10, 100),
                    shipping_details=f'Free shipping on orders over $50. Estimated delivery: 3-5 business days.'
                )
                product_count += 1

                # Create 2-4 images per product
                num_images = random.randint(2, 4)
                for img_idx in range(num_images):
                    image_url = self.get_image_url(f"{category}_{name}", img_idx)
                    filename = f"{category.lower().replace(' ', '_')}_{idx}_{img_idx}.jpg"

                    image_content = self.download_image(image_url, filename)
                    if image_content:
                        ProductImage.objects.create(
                            product=product,
                            image=image_content
                        )
                        image_count += 1
                        self.stdout.write(f'  Created image {img_idx + 1} for: {name}')
                    else:
                        self.stdout.write(self.style.WARNING(f'  Skipped image for: {name}'))

                self.stdout.write(self.style.SUCCESS(f'  Created: {name}'))

        self.stdout.write(self.style.SUCCESS(f'\nSeed complete!'))
        self.stdout.write(self.style.SUCCESS(f'Products created: {product_count}'))
        self.stdout.write(self.style.SUCCESS(f'Images created: {image_count}'))
