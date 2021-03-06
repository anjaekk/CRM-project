import React from 'react';

// ATOMS, ORGANISMS
import { Span, Select, Input } from '../../../Components/Atoms';
import EditableTable from '../../../Components/Atoms/EditableTable';

// STYLES
import styled from 'styled-components';

function index({ column, data, data_search }) {
  return (
    <TempleteEle>
      <Span size="h1">Contact</Span>
      <SelectInput>
        <Select size="mid" selectLists={data_search} />
        <Input type="text" placeholder="Select and Search" name="search" />
      </SelectInput>
      <EditableTable column={column} data={data} />
    </TempleteEle>
  );
}

export default index;

const TempleteEle = styled.div`
  ${({ theme }) => theme.flex('center', 'center', 'column')}
`;
const SelectInput = styled.div`
  ${({ theme }) => theme.flex('center', 'center', null)}
`;
