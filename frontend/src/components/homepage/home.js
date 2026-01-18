import React from 'react'
import { Box, IconButton } from '@mui/material'
import SlidingPage from '../slidingpage/slidingpage'
import ProductCard from '../productcard/productCard'
import ArrowCircleLeftIcon from '@mui/icons-material/ArrowCircleLeft';
import ArrowCircleRightIcon from '@mui/icons-material/ArrowCircleRight';

function Home ({
  products,
  handleSlide,
  currentIndex,
  fetchCartProducts,
  toggleWishlist,
  userWishlistProducts,
  handleAddToCart
}) {
  const visibleProducts = products.slice(currentIndex, currentIndex + 4)
  return (
    <Box style={homeStyles.homePage}>
      <SlidingPage />
      <Box style={homeStyles.catalogContainer}>
        <Box style={homeStyles.productsRow}>
          {visibleProducts.map((product, index) => (
            <ProductCard
              key={index}
              product={product}
              fetchCartProducts={fetchCartProducts}
              toggleWishlist={toggleWishlist}
              userWishlistProducts={userWishlistProducts}
              handleAddToCart={handleAddToCart}
            />
          ))}
        </Box>
        <Box style={homeStyles.sliderControls}>
          <IconButton 
            sx={homeStyles.prevNextButton} 
            onClick={() => handleSlide('prev')}
          ><ArrowCircleLeftIcon/></IconButton>
          <IconButton 
            sx={homeStyles.prevNextButton} 
            onClick={() => handleSlide('next')}
          ><ArrowCircleRightIcon/></IconButton>
        </Box>
      </Box>
    </Box>
  )
}

const homeStyles = {
  homePage: {
    marginTop: '70px',
    marginBottom: '20px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center'
  },
  catalogContainer: {
    marginTop: '20px',
    padding: '0 20px'
  },
  productsRow: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
    justifyItems: 'center',
    width: '100%',
    maxWidth: '1400px',
    margin: '0 auto',
    gap: '30px',
    padding: '10px'
  },
  sliderControls: {
    display: 'flex',
    justifyContent: 'center',
    marginTop: '20px',
    gap: '10px'
  },
  prevNextButton: {
    color: 'white',
    backgroundColor: '#144981',
    '&:hover': {
      backgroundColor: 'white',
      color: '#144981'
    }
  },
}

export default Home
