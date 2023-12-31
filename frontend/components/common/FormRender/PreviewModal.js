import React from "react";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import CloseIcon from '@mui/icons-material/Close';

export default function PreviewModal({ open, onClose, children }) {

  const modalStyle = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    width: '80vw',
    transform: 'translate(-50%, -50%)',
    bgcolor: 'background.paper',
    boxShadow: 24,
    maxHeight: '80%',
    overflowY: 'auto',
    p: '2em 9em',
  };

  const iconStyle = {
    position: 'absolute',
    top: '1em',
    right: '1em'
  }


  return (
    <Modal open={open} onClose={onClose} data-testid="PreviewModal">
      <Box sx={modalStyle}>
        <CloseIcon onClick={onClose} cursor="pointer" sx={iconStyle}/>
        {children}
      </Box>
    </Modal>
  )
}
