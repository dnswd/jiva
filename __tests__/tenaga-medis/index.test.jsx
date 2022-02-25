import { render, screen } from '@testing-library/react'
import DashboardTenagaMedis from 'pages/tenaga-medis/index'
import '@testing-library/jest-dom'

describe('Dashboard Tenaga Medis Main Components', () => {
  it('should render', () => {
    render(<DashboardTenagaMedis />)

    const main = screen.getByRole('main')

    expect(main).toBeInTheDocument()
  })


  it('should have the page main heading', () => {
    render(<DashboardTenagaMedis />)

    const heading = screen.getByRole('heading', {
      name: /Daftar Tenaga Medis/,
    })

    expect(heading).toBeInTheDocument()
  })


  it('should have the tenaga medis list table', () => {
    render(<DashboardTenagaMedis />)

    const table = screen.getByRole('table')
    
    expect(table).toBeInTheDocument()
  })


  it('should have the tambah tenaga medis button', () => {
    render(<DashboardTenagaMedis />)

    const button = screen.getByRole('button', {
      name: /Tambah Tenaga Medis/,
    })

    expect(button).toBeInTheDocument()
  })
})



describe('Tenaga medis list table properties', () => {
  it('should have the appropriate columns', () => {
    render(<DashboardTenagaMedis />)

    const namaColumn = screen.getByRole('columnheader', {
      name: /Nama/,
    })
    const ttlColumn = screen.getByRole('columnheader', {
      name: /Tempat\/Tanggal Lahir/,
    })
    const nikColumn = screen.getByRole('columnheader', {
      name: /NIK/,
    })
    const lihatColumn = screen.getByRole('columnheader', {
      name: /^$/,
    })
    
    expect(namaColumn).toBeInTheDocument()
    expect(ttlColumn).toBeInTheDocument()
    expect(nikColumn).toBeInTheDocument()
    expect(lihatColumn).toBeInTheDocument()
  })
})
